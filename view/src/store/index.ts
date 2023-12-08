import { createStore } from "vuex";
import athModule from './modules/auth/index.ts';
import chatModule from './modules/chat/index.ts';

const store = createStore({
    modules: {
        auth: athModule,
        chat: chatModule
    },
    state() {
        return {
            apiUrl: 'http://localhost:8000/api/'
        }
    },
    getters: {
        getApiUrl(state) {
            return state.apiUrl;
        }
    }
})

export default store;