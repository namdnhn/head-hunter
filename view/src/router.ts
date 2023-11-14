import { createRouter, createWebHistory } from "vue-router";
import { defineAsyncComponent } from "vue";
import store from "./store/index.ts";

//import page
const HomePage = defineAsyncComponent(() => import("./pages/HomePage.vue"));
const ProfilePage = defineAsyncComponent(
	() => import("./pages/user/ProfilePage.vue")
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
const CompanySearchPage = defineAsyncComponent(
	() => import("./pages/company/CompanySearchPage.vue")
);
const CompanyDetailPage = defineAsyncComponent(
	() => import("./pages/company/CompanyDetail.vue")
);
const EmployeeDashboard = defineAsyncComponent(
	() => import("./pages/dashboard/DashBoard.vue")
);
const UserDashboard = defineAsyncComponent(
	() => import("./pages/dashboard/UserDashboard.vue")
);
const UserInfo = defineAsyncComponent(
	() => import("./pages/dashboard/UserInfo.vue")
);
const JobSaved = defineAsyncComponent(
	() => import("./pages/dashboard/JobSaved.vue")
);
const CompanySaved = defineAsyncComponent(
	() => import("./pages/dashboard/CompanySaved.vue")
);

const UpdateAccount = defineAsyncComponent(
	() => import("./pages/dashboard/UpdateAccount.vue")
);

const DeleteAccount = defineAsyncComponent(
	() => import("./pages/dashboard/DeleteAccount.vue")
);

const ChatPage = defineAsyncComponent(() => import("./pages/dashboard/ChatPage.vue"));

const NotFound = defineAsyncComponent(() => import("./pages/404Page.vue"));

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
		{ path: "/companysearch", component: CompanySearchPage },
		{ path: "/companydetail/:id", component: CompanyDetailPage },
		{ path: "/employeedashboard", component: EmployeeDashboard },
		{
			path: "/userdashboard",
			redirect: "/userdashboard/userinfo",
			component: UserDashboard,
			meta: { requiresAuth: true },
			children: [
				{
					path: "/userdashboard/userinfo",
					component: UserInfo,
					meta: { requiresAuth: true },
				},
				{
					path: "/userdashboard/jobsaved",
					component: JobSaved,
					meta: { requiresAuth: true },
				},
				{
					path: "/userdashboard/companysaved",
					component: CompanySaved,
					meta: { requiresAuth: true },
				},
				{
					path: "/userdashboard/updateaccount",
					component: UpdateAccount,
					meta: { requiresAuth: true },
				},
				{
					path: "/userdashboard/deleteaccount",
					component: DeleteAccount,
					meta: { requiresAuth: true },
				},
                {
                    path: "/userdashboard/chat",
                    component: ChatPage,
                    meta: { requiresAuth: true },
                },
			],
		},
		{
			path: "/:pathMatch(.*)*",
			component: NotFound,
		},
	],
	scrollBehavior() {
		return { top: 0, behavior: "smooth" };
	},
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
