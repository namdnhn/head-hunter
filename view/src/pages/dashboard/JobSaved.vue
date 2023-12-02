<template>
	<div class="p-8 md:basis-3/5 lg:basis-4/5 flex flex-col gap-10">
		<h1 class="text-lg md:text-xl lg:text-2xl text-sky-900 font-bold">
			Tin tuyển dụng đã lưu
		</h1>
		<div class="w-full p-10 bg-white rounded-xl flex flex-col gap-4">
            <h2 class="text-base md:text-lg lg:text-xl font-semibold text-sky-900">Đã lưu {{ quantity }} tin tuyển dụng</h2>
			<saved-card
				v-for="job in jobs"
				:key="job.id"
				:logo="job.logo"
				:name="job.name"
				:location="job.location"    
				:expire="job.expire"
                type="job"
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
			jobs: [
				{
					id: 1,
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					name: "Sun* Inc",
					location: "Cau Giay, Ha Noi",
					expire: "23/10/2023",
				},
				{
					id: 2,
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					name: "Sun* Inc",
					location: "Cau Giay, Ha Noi",
					expire: "23/10/2023",
				},
			],
		};
	},
    computed: {
        quantity() {
            return this.jobs.length
        }
    }
};
</script>
