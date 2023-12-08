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
            companyId: null,
            companyInfo: {
                name: null,
                email: null,
                
            }
        }
    },
    actions,
    mutations,
    getters
}