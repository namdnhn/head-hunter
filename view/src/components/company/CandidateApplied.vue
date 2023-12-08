<template>
	<div class="p-8 md:basis-3/5 lg:basis-4/5 flex flex-col gap-10">
		<h1 class="text-lg md:text-xl lg:text-2xl text-sky-900 font-bold">
			Ứng viên đã ứng tuyển
		</h1>
		<div class="w-full p-10 bg-white rounded-xl flex flex-col gap-4">
            <h2 class="text-base md:text-lg lg:text-xl font-semibold text-sky-900">Danh sách {{ quantity }} ứng viên đã ứng tuyển</h2>
			<applied-job
				v-for="candidate in candidates"
				:key="candidate.id"
				:logo="candidate.logo"
				:name="candidate.name"
				:position="candidate.position"
                type="candidate"
			></applied-job>
		</div>
	</div>
</template>

<script lang="ts">
// import SavedCard from "../../components/dashboard/SavedCard.vue";
import AppliedJob from "../../components/dashboard/AppliedJob.vue"
export default {
	components: {
		// SavedCard,
		AppliedJob
	},
	data() {
		return {
			candidates: [
				{
					id: 1,
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					name: "Nguyen Duc Thien",
					position: "Backend Developer",
				},
				{
					id: 2,
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					name: "Nguyen Van A",
					position: "Fullstack Developer",
				},
			],
		};
	},
    computed: {
        quantity() {
            return this.candidates.length
        }
    }
};
</script>
