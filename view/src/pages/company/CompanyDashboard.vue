<template>
	<main class="pt-16 lg:pt-20 w-full flex flex-col lg:flex-row bg-slate-200">
		<company-sidebar></company-sidebar>
		<router-view v-slot="slotProps">
			<transition name="route" mode="out-in">
				<component :is="slotProps.Component"></component>
			</transition>
		</router-view>
	</main>
</template>

<script lang="ts">
import CompanySidebar from "../../components/company/CompanySidebar.vue";
export default {
	components: {
		CompanySidebar
	},
};
</script>
