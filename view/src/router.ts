import { createRouter, createWebHistory } from "vue-router";
import { defineAsyncComponent } from "vue";
import store from "./store/index.ts";

//import page
const HomePage = defineAsyncComponent(() => import("./pages/HomePage.vue"));
const ProfilePage = defineAsyncComponent(
	() => import("./pages/ProfilePage.vue")
);
const LoginCandicatePage = defineAsyncComponent(
	() => import("./pages/auth/LoginCandicatePage.vue")
);
const RegisterCandicatePage = defineAsyncComponent(
	() => import("./pages/auth/RegisterCandicatePage.vue")
);
const LoginEmployeePage = defineAsyncComponent(
	() => import("./pages/auth/LoginEmployeePage.vue")
);
const RegisterEmployeePage = defineAsyncComponent(
	() => import("./pages/auth/RegisterEmployeePage.vue")
);
const ResetPasswordCandicate = defineAsyncComponent(
	() => import("./pages/auth/ResetPasswordCandicate.vue")
);
const ResetPasswordEmployee = defineAsyncComponent(
	() => import("./pages/auth/ResetPasswordEmployee.vue")
);
const JobDetail = defineAsyncComponent(
	() => import("./pages/jobs/JobDetail.vue")
);
const JobSearch = defineAsyncComponent(
	() => import("./pages/jobs/JobSearch.vue")
);

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{ path: "/", redirect: "/homepage" },
		{
			path: "/homepage",
			component: HomePage,
		},
		{
			path: "/profile",
			component: ProfilePage,
			meta: { requiresAuth: true },
		},
		{
			path: "/loginCandidatePage",
			component: LoginCandicatePage,
			meta: { requiresUnAuth: true },
		},
		{
			path: "/registerEmployeePage",
			component: RegisterEmployeePage,
			meta: { requiresUnAuth: true },
		},
		{
			path: "/loginEmployeePage",
			component: LoginEmployeePage,
			meta: { requiresUnAuth: true },
		},
		{
			path: "/registerCandidatePage",
			component: RegisterCandicatePage,
			meta: { requiresUnAuth: true },
		},
		{
			path: "/resetPasswordCandidate",
			component: ResetPasswordCandicate,
			meta: { requiresUnAuth: true },
		},
		{
			path: "/resetPasswordEmployee",
			component: ResetPasswordEmployee,
			meta: { requiresUnAuth: true },
		},
		{
			path: "/jobdetail/:id",
			component: JobDetail,
		},
		{
			path: "/jobsearch",
			component: JobSearch,
		},
	],
});

router.beforeEach(function (to, _, next) {
	if (to.meta.requiresAuth && !store.getters.isAuthenticated) {
		next("/loginCandidatePage");
	} else if (to.meta.requiresUnAuth && store.getters.isAuthenticated) {
		next("/homepage");
	} else {
		next();
	}
});

export default router;
