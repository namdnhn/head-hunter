type AuthPayload = {
	email: string;
	password: string;
	fullname: string;
	phone: string;
	mode: string;
	date_of_birth: string;
}

let timer: string | number | NodeJS.Timeout | undefined;

export default {
	async auth(context: any, payload: AuthPayload) {
		const mode = payload.mode;
		let apiUrl = await context.rootGetters.getApiUrl;
		let data = {};

		if (mode === "register") {
			apiUrl += "register";
			data = {
				email: payload.email,
				password: payload.password,
				fullname: payload.fullname,
				date_of_birth: payload.date_of_birth,
				phone: payload.phone,
			};
		} else if (mode === "login") {
			apiUrl += "login";
			data = {
				email: payload.email,
				password: payload.password,
			};
		}

		const response = await fetch(apiUrl, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(data),
		});

		const responseData = await response.json();

		if (!response.ok) {
			let error;
			if (response.status === 404 && mode === 'login') {
				error = new Error("Email hoặc mật khẩu không chính xác!");
			} else {
				error = new Error(responseData.message || "Có lỗi không xác định đã xảy ra!");
			}
			throw error;
		}

		const expiresIn = new Date().getTime() + 259200000;

		localStorage.setItem("token", responseData.jwtToken);
		localStorage.setItem("expiresIn", expiresIn.toString());

		timer = setTimeout(() => {
			context.dispatch("autoLogout");
		}, expiresIn);

		if (mode === "register") {
			localStorage.setItem("userId", responseData.user.id);
			context.commit("setUser", {
				token: responseData.jwtToken,
				userId: responseData.user.id,
			});
		} else if (mode === "login") {
			localStorage.setItem("userId", responseData.id);
			context.commit("setUser", {
				token: responseData.jwtToken,
				userId: responseData.id,
			});
		}
	},

	autoLogin(context: any) {
		const token = localStorage.getItem("token");
		const userId = localStorage.getItem("userId");
		const expiresIn = Number(localStorage.getItem("expiresIn"));

		const liveTime = +expiresIn - new Date().getTime();
		if (liveTime <= 0) {
			return;
		}

		timer = setTimeout(() => {
			context.dispatch("autoLogout");
		}, expiresIn);

		if (token) {
			context.commit("setUser", {
				token: token,
				userId: userId,
			});
		}
	},

	logout(context: any) {
		clearTimeout(timer);

		localStorage.removeItem("token");
		localStorage.removeItem("userId");
		localStorage.removeItem("expiresIn");

		context.commit("setUser", {
			token: null,
			userId: null,
		});
	},

	autoLogout(context: any) {
		context.dispatch("logout");
		context.commit("setLogout");
	},

	setAutoLogout(state: any) {
		state.didAutoLogout = true;
	},

	async fetchUserById(context: any, id: Number) {
		let apiUrl = await context.rootGetters.getApiUrl;
		apiUrl += `user/${id}`;
		const response = await fetch(apiUrl, {
			method: 'GET',
			headers: {
				"Content-Type": "application/json",
			},
		})

		const responseData = await response.json();

		if(!response.ok) {
			const error = new Error(responseData.message || "Lỗi lấy dữ liệu người dùng");
			throw error;
		}

		const payload = {
			fullname: responseData.fullname,
			phone: responseData.phone,
			date_of_birth: responseData.date_of_birth,
			email: responseData.email,
		}

		context.commit('setUserInfo', payload);
	}
};
