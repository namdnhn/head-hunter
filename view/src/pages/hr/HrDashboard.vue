<template>
	<main class="pt-16 lg:pt-20 w-full flex flex-col lg:flex-row bg-slate-200">
		<hr-sidebar></hr-sidebar>
		<router-view v-slot="slotProps">
			<transition name="route" mode="out-in">
				<component :is="slotProps.Component"></component>
			</transition>
		</router-view>
	</main>
</template>

<script lang="ts">
import HrSidebar from "../../components/hr/HrSidebar.vue";
export default {
	components: {
		HrSidebar
	},
};
</script>
