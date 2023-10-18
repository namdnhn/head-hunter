interface authState {
    token: string | null;
    userId: string | null;
}

interface authPayload {
    token: string | null;
    userId: string | null;
}

export default {
    setUser(state: authState, payload: authPayload) {
        state.token = payload.token;
        state.userId = payload.userId;
    }
}