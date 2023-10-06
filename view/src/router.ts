import { createRouter, createWebHistory } from "vue-router";

//import page
// const HomePage = defineAsyncComponent(() => import("./pages/HomePage.vue"));
import HomePage from "./pages/HomePage.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', redirect: "/homepage"},
        { path: '/homepage', component: HomePage},
    ]
})

export default router;