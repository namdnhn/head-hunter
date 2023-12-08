type AuthPayload = {
	email: string;
	password: string;
	fullname: string;
	phone: string;
	mode: string;
	date_of_birth: string;
};

let timer: string | number | NodeJS.Timeout | undefined;

export default {
	async auth(context: any, payload: AuthPayload) {
		const mode = payload.mode;
		let apiUrl = await context.rootGetters.getApiUrl;
		let data = {};

		if (mode === "register") {
			apiUrl += "register";
			data = {
				fullname: payload.fullname,
				image_path: "string",
				email: payload.email,
				password: payload.password,
				date_of_birth: payload.date_of_birth,
				gender: "male",
				role: "candidate",
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
			if (responseData.detail === "Incorrect password") {
				error = new Error("Mật khẩu không chính xác!");
			} else if (responseData.detail === "Invalid Credentials") {
				error = new Error("Email không tồn tại!");
			} else {
				error = new Error("Lỗi không xác định đã xảy ra!");
			}

			throw error;
		}

		const expiresIn = new Date().getTime() + 259200000;

		localStorage.setItem("token", responseData.jwtToken);
		localStorage.setItem("expiresIn", expiresIn.toString());
		localStorage.setItem("role", responseData.role);

		clearTimeout(timer);
		//expiresIn = 3 days
		timer = setTimeout(() => {
			context.dispatch("autoLogout");
		}, 259200000);

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

			context.commit("setUserInfo", {
				fullname: responseData.fullname,
				phone: responseData.phone,
				date_of_birth: responseData.date_of_birth,
				email: responseData.email,
			});

			if (responseData.role === "hr") {
				//get company by user id
				let api = await context.rootGetters.getApiUrl;
				api += `company/user/${responseData.id}`;

				const response = await fetch(api, {
					method: "GET",
					headers: {
						"Content-Type": "application/json",
					},
				});

				const responseCompanyData = await response.json();

				if (!response.ok) {
					const error = new Error(
						responseCompanyData.message || "Lỗi lấy dữ liệu công ty"
					);
					throw error;
				}

				localStorage.setItem("companyId", responseCompanyData.id);

				context.commit("setCompanyId", responseCompanyData.id);
				context.commit("setCompanyInfo", {
					name: responseCompanyData.name,
					email: responseCompanyData.email,
				});
			}
		}
	},

	autoLogin(context: any) {
		const token = localStorage.getItem("token");
		const userId = localStorage.getItem("userId");

		if (token) {
            context.commit("setUser", {
                token: token,
                userId: userId,
            });
		}
	},

	logout(context: any) {
		console.log("logout");

		clearTimeout(timer);

		localStorage.removeItem("token");
		localStorage.removeItem("userId");
		localStorage.removeItem("expiresIn");
		localStorage.removeItem("role");
		localStorage.removeItem("companyId");

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
			method: "GET",
			headers: {
				"Content-Type": "application/json",
			},
		});

		const responseData = await response.json();

		if (!response.ok) {
			const error = new Error(
				responseData.message || "Lỗi lấy dữ liệu người dùng"
			);
			throw error;
		}

		// const dob = new Date(
		// 	Date.parse(responseData.date_of_birth)
		// ).toLocaleDateString("en-GB");

		//is candidate
		if (responseData.role === "candidate") {
			const payload = {
				fullname: responseData.fullname,
				phone: responseData.phone,
				date_of_birth: responseData.date_of_birth,
				email: responseData.email,
			};

			context.commit("setUserInfo", payload);

		}

		if (responseData.role === "hr") {
			const payload = {
				fullname: responseData.fullname,
				email: responseData.email,
			};

			context.commit("setCompanyInfo", payload);

            context.commit("setCompanyId", responseData.company_id)
		}

		return responseData;
	},

	//update info
	async updateInfo(context: any, payload: AuthPayload) {
		const apiUrl = await context.rootGetters.getApiUrl;
		const userId = localStorage.getItem("userId");

		const data = {
			email: payload.email,
			password: payload.password,
			fullname: payload.fullname,
			date_of_birth: payload.date_of_birth,
			phone: payload.phone,
		};

		const response = await fetch(`${apiUrl}user/update/${userId}`, {
			method: "PUT",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(data),
		});

		const responseData = await response.json();

		if (!response.ok) {
			const error = new Error(
				responseData.message || "Có lỗi không xác định đã xảy ra!"
			);
			throw error;
		}

		context.commit("setUserInfo", data);
	},

	//register company
	async registerCompany(context: any, payload: any) {
		let apiUrl = await context.rootGetters.getApiUrl;
		apiUrl += "register";

		console.log(payload);

		const response = await fetch(apiUrl, {
			method: "POST",
			body: JSON.stringify({
				fullname: payload.fullname,
				image_path: "string",
				email: payload.email,
				password: payload.password,
				date_of_birth: "2023-12-07T08:16:46.167Z",
				gender: "male",
				role: "hr",
				phone: "string",
			}),
			headers: {
				"Content-Type": "application/json",
			},
		});

		console.log(response);

		const responseData = await response.json();

		if (!response.ok) {
			const error = new Error(
				responseData.message || "Failed to create company."
			);
			throw error;
		}

		const companyInfo = {
			accountId: responseData.accountId,
			companyId: payload.companyId,
			email: responseData.email,
			name: responseData.name,
		};

		context.commit("setCompanyInfo", companyInfo);

		return responseData.user;
	},
};
