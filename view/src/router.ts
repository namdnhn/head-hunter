import { createRouter, createWebHistory } from "vue-router";
import { defineAsyncComponent } from "vue";

//import page
const HomePage = defineAsyncComponent(() => import("./pages/HomePage.vue"));
const ProfilePage = defineAsyncComponent(() => import("./pages/ProfilePage.vue"));
const LoginPage = defineAsyncComponent(() => import("./pages/auth/LoginPage.vue"))
const RegisterPage = defineAsyncComponent(() => import("./pages/auth/RegisterPage.vue"))

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", redirect: "/homepage" },
    { path: "/homepage", component: HomePage },
    { path: "/profile", component: ProfilePage },
    { path: "/login", component: LoginPage},
    { path: "/register", component: RegisterPage}
  ],
}); 

export default router;
