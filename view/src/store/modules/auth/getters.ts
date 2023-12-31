interface AuthState {
    token: string | null
    userId: string | null
}

type UserInfo = {
    fullname: string
    phone: string
    date_of_birth: string
    email: string
}


export default {
    token(state: AuthState) {
        return state.token;
    },
    userId(state: AuthState) { 
        return state.userId;
    },
    isAuthenticated(state: AuthState) {
        return !!state.token;
    },
    getUserInfo(state: { userInfo: UserInfo }) {
        return state.userInfo;
    },
    isCompany(state: any) {
        return !!state.companyId
    },
    companyId(state: any) {
        return state.companyId;
    },
    isCandidate(state: any) {
        return !!state.userInfo
    }
}