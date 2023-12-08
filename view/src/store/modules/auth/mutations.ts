interface authState {
	token: string | null;
	userId: string | null;
}

interface authPayload {
	token: string | null;
	userId: string | null;
}

type UserInfo = {
	fullname: string;
	phone: string;
	date_of_birth: string;
	email: string;
};

export default {
	setUser(state: authState, payload: authPayload) {
		state.token = payload.token;
		state.userId = payload.userId;
	},
	setLogout(state: authState) {
		state.token = null;
		state.userId = null;
	},
	setUserInfo(state: { userInfo: UserInfo }, payload: UserInfo) {
		state.userInfo = payload;
	},
    setCompanyId(state: any, id: any) {
        state.companyId = id;
    },
    setCompanyInfo(state: any, payload: any) {
        state.companyInfo = payload;
    }
};
