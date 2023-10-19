import actions from "./actions.ts";
import mutations from "./mutations.ts";
import getters from "./getters.ts";

export default {
    state() {
        return {
            token: null,
            userId: null,
            didAutoLogout: false
        }
    },
    actions,
    mutations,
    getters
}