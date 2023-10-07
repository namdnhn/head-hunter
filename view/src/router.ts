import { createRouter, createWebHistory } from "vue-router";
import { defineAsyncComponent } from "vue";

//import page
const HomePage = defineAsyncComponent(() => import("./pages/HomePage.vue"));
const ProfilePage = defineAsyncComponent(
  () => import("./pages/ProfilePage.vue")
);

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", redirect: "/homepage" },
    { path: "/homepage", component: HomePage },
    { path: "/profile", component: ProfilePage },
  ],
}); 

export default router;
