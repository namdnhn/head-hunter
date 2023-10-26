<template>
	<main class="pt-16 lg:pt-20 w-full h-screen flex flex-col md:flex-row bg-slate-200">
		<side-bar></side-bar>
		<router-view></router-view>
	</main>
</template>

<script lang="ts">
import SideBar from "../../components/dashboard/SideBar.vue";
export default {
	components: {
		SideBar,
	},
};
</script>
