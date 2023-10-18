interface AuthState {
    token: string | null
    userId: string | null
}

export default {
    token(state: AuthState) {
        return state.token;
    },
    userId(state: AuthState) { 
        return state.userId;
    }
}