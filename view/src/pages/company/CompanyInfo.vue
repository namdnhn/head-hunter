<template>
	<div class="p-8 md:basis-3/5 lg:basis-4/5 flex flex-col gap-10 min-h-screen max-h-screen overflow-y-auto">
		<h1 class="text-lg md:text-xl lg:text-2xl text-sky-900 font-bold">
			Thông tin người dùng
		</h1>
		<div
			class="w-full grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-2 gap-4"
		>
			<!-- Applied job -->
			<statistic-card
				icon="fa-solid fa-briefcase"
				color="bg-green-100 text-green-600"
				title="524"
				subtitle="Ứng viên đã ứng tuyển"
			></statistic-card>

			<!-- Saved job -->
			<statistic-card
				icon="fa-solid fa-bookmark"
				color="bg-yellow-100 text-amber-500 px-5"
				title="120"
				subtitle="Ứng viên đã lưu"
			></statistic-card>

			<!-- Viewd profile  -->
			
		</div>

		<!-- notification and applied job -->
		<div class="flex flex-col lg:flex-row gap-4 w-full">
			<!-- notification  -->
			<div class="bg-white p-4 rounded-lg lg:basis-1/3">
				<h1
					class="mb-4 text-sm md:text-base lg:text-xl font-semibold text-sky-900"
				>
					Thông báo
				</h1>
				<notify-card
					type="reply"
					title="Nguyễn Đức Thiện"
					subtitle="Đã trả lời tin nhắn của bạn"
					time="Bây giờ"
				></notify-card>
				<notify-card
					type="approve"
					title="Nguyễn Đức Thiện"
					subtitle="Đã nộp hồ sơ"
					time="3 giờ trước"
				></notify-card>
				<notify-card
					type="receive"
					title="Sun* Inc"
					subtitle="Đã gửi tin nhắn cho bạn"
					time="5 giờ trước"
				></notify-card>
			</div>

			<!-- applied job  -->
			<div
				class="bg-white p-4 rounded-lg lg:basis-2/3 flex flex-col gap-4"
			>
				<h1
					class="mb-4 text-sm md:text-base lg:text-xl font-semibold text-sky-900"
				>
					Ứng viên đang ứng tuyển
				</h1>

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
	</div>
</template>

<script lang="ts">
import StatisticCard from "../../components/dashboard/StatisticCard.vue";
import NotifyCard from "../../components/dashboard/NotifyCard.vue";
import CandidateApplied from "../../components/company/CandidateApplied.vue";
import AppliedJob from "../../components/dashboard/AppliedJob.vue"
export default {
	components: {
		StatisticCard,
		NotifyCard,
		CandidateApplied,
		AppliedJob
	},
	data() {
		return {
			candidates: [
				{
					id: 1,
					name: "Nguyen Duc Thien",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					position: "Backend Developer",
					time: "23/10/2023",
					status: "Chấp nhận",
				},
				{
					id: 2,
					name: "Nguyen Van A",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					position: "Backend Developer",
					time: "23/10/2023",
					status: "Đang chờ",
				},
				{
					id: 3,
					name: "Hoang Van B",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					position: "Backend Developer",
					time: "23/10/2023",
					status: "Từ chối",
				},
			],
		};
	},
};
</script>
