<template>
	<main class="pt-16 lg:pt-20 w-full flex flex-col lg:flex-row bg-slate-200">
		<side-bar></side-bar>
		<router-view v-slot="slotProps">
			<transition name="route" mode="out-in">
				<component :is="slotProps.Component"></component>
			</transition>
		</router-view>
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
