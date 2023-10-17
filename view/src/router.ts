import { createRouter, createWebHistory } from "vue-router";
import { defineAsyncComponent } from "vue";

//import page
const HomePage = defineAsyncComponent(() => import("./pages/HomePage.vue"));
const ProfilePage = defineAsyncComponent(() => import("./pages/ProfilePage.vue"));
const LoginCandicatePage = defineAsyncComponent(() => import("./pages/auth/LoginCandicatePage.vue"))
const RegisterCandicatePage = defineAsyncComponent(() => import("./pages/auth/RegisterCandicatePage.vue"))
const LoginEmployeePage = defineAsyncComponent(() => import("./pages/auth/LoginEmployeePage.vue"))
const RegisterEmployeePage = defineAsyncComponent(() => import("./pages/auth/RegisterEmployeePage.vue"))
const ResetPasswordCandicate = defineAsyncComponent(() => import("./pages/auth/ResetPasswordCandicate.vue"))
const ResetPasswordEmployee = defineAsyncComponent(() => import("./pages/auth/ResetPasswordEmployee.vue"))
const JobDetail = defineAsyncComponent(() => import("./pages/jobs/JobDetail.vue"))
const JobSearch = defineAsyncComponent(() => import("./pages/jobs/JobSearch.vue"))

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", redirect: "/homepage" },
    { path: "/homepage", component: HomePage },
    { path: "/profile", component: ProfilePage },
    { path: "/loginCandidatePage", component: LoginCandicatePage},
    { path: "/registerEmployeePage", component: RegisterEmployeePage},
    { path: "/loginEmployeePage", component: LoginEmployeePage},
    { path: "/registerCandidatePage", component: RegisterCandicatePage},
    { path: "/resetPasswordCandicate", component: ResetPasswordCandicate},
    { path: "/resetPasswordEmployee", component: ResetPasswordEmployee},
    {path: "/jobdetail/:id", component: JobDetail},
    {path: "/jobsearch", component: JobSearch}
  ],
}); 

export default router;
