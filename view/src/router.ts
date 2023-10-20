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
const CompanySearchPage = defineAsyncComponent(() => import("./pages/CompanySearchPage.vue"))
const CompanyDetailPage = defineAsyncComponent(() => import("./pages/CompanyDetail.vue"))

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", redirect: "/homepage" },
    { path: "/homepage", component: HomePage },
    { path: "/profile", component: ProfilePage },
    { path: "/loginCandicatePage", component: LoginCandicatePage},
    { path: "/registerEmployeePage", component: RegisterEmployeePage},
    { path: "/loginEmployeePage", component: LoginEmployeePage},
    { path: "/registerCandicatePage", component: RegisterCandicatePage},
    { path: "/resetPasswordCandicate", component: ResetPasswordCandicate},
    { path: "/resetPasswordEmployee", component: ResetPasswordEmployee},
    { path: "/companySearchPage", component: CompanySearchPage},
    { path: "/companyDetailPage", component: CompanyDetailPage}
  ],
}); 

export default router;
