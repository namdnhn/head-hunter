import { createStore } from "vuex";
import athModule from './modules/auth/index.ts';
import jobsModule from './modules/jobs/index.ts';
import companiesModule from './modules/companies/index.ts';
import cvModule from './modules/cv/index.ts';

const store = createStore({
    modules: {
        auth: athModule,
        jobs: jobsModule,
        companies: companiesModule,
        cv: cvModule
    },
    state() {
        return {
            apiUrl: 'http://localhost:8000/api/',
        }
    },
    getters: {
        getApiUrl(state) {
            return state.apiUrl;
        }
    }
})

export default store;