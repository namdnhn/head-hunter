import { createRouter, createWebHistory } from "vue-router";
import { defineAsyncComponent } from "vue";
import store from "./store/index.ts";

//import page
const HomePage = defineAsyncComponent(() => import("./pages/HomePage.vue"));
const ContactPage = defineAsyncComponent(() => import("./pages/about/ContactPage.vue"))
const IntroductionPage = defineAsyncComponent(() => import("./pages/about/IntroductionPage.vue"))
const SupportPage = defineAsyncComponent(() => import("./pages/about/SupportPage.vue"))
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

const ChatPage = defineAsyncComponent(
	() => import("./pages/dashboard/ChatPage.vue")
);

const NotFound = defineAsyncComponent(() => import("./pages/404Page.vue"));

const CandidateSearch = defineAsyncComponent(
	() => import("./pages/company/CandidateSearch.vue")
);

const CompanyInfo = defineAsyncComponent(
	() => import("./pages/company/CompanyInfo.vue")
);

const CompanyDashboard = defineAsyncComponent(
	() => import("./pages/company/CompanyDashboard.vue")
);

const CandidateSaved = defineAsyncComponent(
	() => import("./pages/company/CandidateSaved.vue")
);

const CompanyProfile = defineAsyncComponent(
	() => import("./pages/company/CompanyProfile.vue")
);

const UpdateCompanyInfo = defineAsyncComponent(
	() => import("./pages/company/UpdateInfo.vue")
);

const RecruitmentPost = defineAsyncComponent(
	() => import("./pages/company/RecruitmentPost.vue")
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
			path:"/introductionpage",
			component: IntroductionPage,
		},
		{
			path:"/supportpage",
			component: SupportPage,
		},
		{
			path:"/contactpage",
			component: ContactPage,
		},
		{
			path: "/profile/:id",
			component: ProfilePage,
			meta: { requiresAuth: true },
		},
		{
			path: "/loginCandidatePage",
			component: LoginCandicatePage,
			meta: { requiresUnAuth: true },
		},
		{
			path: "/register/employee",
			component: RegisterEmployeePage,
			meta: { requiresUnAuth: true },
		},
		{
			path: "/login/employee",
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
            props: true,
		},
		{
			path: "/jobsearch",
			component: JobSearch,
		},
		{ path: "/companysearch", component: CompanySearchPage },
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
			],
		},
		{
			path: "/companydashboard",
			redirect: "/companydashboard/companyinfo",
			component: CompanyDashboard,
			children: [
				{
					path: "/companydashboard/companyinfo",
					component: CompanyInfo,
				},
				{
					path: "/companydashboard/candidatesaved",
					component: CandidateSaved,
				},
				{
					path: "/companydashboard/updatecompany",
					component: UpdateCompanyInfo,
				},
				{
					path: "/companydashboard/deleteaccount",
					component: DeleteAccount,
				},
			],
		},
		{
			path: "/chat",
			component: ChatPage,
			meta: { requiresAuth: true },
		},
		{
			path: "/candidatesearch",
			component: CandidateSearch,
		},
		{
			path: "/companyprofile/:id",
			component: CompanyProfile,
		},
		{
			path: "/companyprofile/:id/recruitmentpost",
			component: RecruitmentPost,
            props: true,
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
