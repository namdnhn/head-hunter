import actions from "./actions.ts";
import mutations from "./mutations.ts";
import getters from "./getters.ts";

export default {
    state() {
        return {
            token: null,
            userId: null,
            didAutoLogout: false,
            userInfo: {
                fullname: null,
                phone: null,
                date_of_birth: null,
                email: null,
            },
            companyInfo: {
                email: null,
                name: null,
                companyId: null,
                accountId: null
            }
        }
    },
    actions,
    mutations,
    getters
}