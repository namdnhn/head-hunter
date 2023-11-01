<template>
	<div class="p-8 md:basis-3/5 lg:basis-4/5 flex flex-col gap-10">
		<h1 class="text-lg md:text-xl lg:text-2xl text-sky-900 font-bold">
			Công ty đang theo dõi
		</h1>
		<div class="w-full p-10 bg-white rounded-xl flex flex-col gap-4">
            <h2 class="text-base md:text-lg lg:text-xl font-semibold text-sky-900">Đang theo dõi {{ quantity }} công ty</h2>
			<saved-card
				v-for="company in companies"
				:key="company.id"
				:logo="company.logo"
				:name="company.name"
				:location="company.location"
			></saved-card>
		</div>
	</div>
</template>

<script lang="ts">
import SavedCard from "../../components/dashboard/SavedCard.vue";
export default {
	components: {
		SavedCard,
	},
	data() {
		return {
			companies: [
				{
					id: 1,
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					name: "Sun* Inc",
					location: "Cau Giay, Ha Noi",
					
				},
				{
					id: 2,
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					name: "Sun* Inc",
					location: "Cau Giay, Ha Noi",
				},
			],
		};
	},
    computed: {
        quantity() {
            return this.companies.length
        }
    }
};
</script>
