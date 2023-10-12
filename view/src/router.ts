import { createRouter, createWebHistory } from "vue-router";
import { defineAsyncComponent } from "vue";

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
const JobDetail = defineAsyncComponent(
	() => import("./pages/jobs/JobDetail.vue")
);

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{ path: "/", redirect: "/homepage" },
		{ path: "/homepage", component: HomePage },
		{ path: "/profile", component: ProfilePage },
		{ path: "/loginCandicatePage", component: LoginCandicatePage },
		{ path: "/registerEmployeePage", component: RegisterEmployeePage },
		{ path: "/loginEmployeePage", component: LoginEmployeePage },
		{ path: "/registerCandicatePage", component: RegisterCandicatePage },
		{ path: "/jobdetail/:id", props: true, component: JobDetail },
	],
});

export default router;
