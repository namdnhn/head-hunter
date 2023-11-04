<template>
	<div class="p-8 md:basis-3/5 lg:basis-4/5 flex flex-col gap-10">
		<h1 class="text-lg md:text-xl lg:text-2xl text-sky-900 font-bold">
			Thông tin người dùng
		</h1>
		<div
			class="w-full grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-4 gap-4"
		>
			<!-- Applied job -->
			<statistic-card
				icon="fa-solid fa-briefcase"
				color="bg-green-100 text-green-600"
				title="523"
				subtitle="Công việc đã ứng tuyển"
			></statistic-card>

			<!-- Saved job -->
			<statistic-card
				icon="fa-solid fa-bookmark"
				color="bg-yellow-100 text-amber-500 px-5"
				title="120"
				subtitle="Công việc đã lưu"
			></statistic-card>

			<!-- Viewd profile  -->
			<statistic-card
				icon="fa-solid fa-eye"
				color="bg-blue-100 text-blue-500"
				title="1.2k"
				subtitle="Lượt xem hồ sơ"
			></statistic-card>

			<!-- reviewd  -->
			<statistic-card
				icon="fa-solid fa-comment"
				color="bg-red-100 text-red-500"
				title="23"
				subtitle="Lượt đánh giá"
			></statistic-card>
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
					title="Sun* Inc"
					subtitle="Đã chấp nhận hồ sơ của bạn"
					time="3 giờ trước"
				></notify-card>
				<notify-card
					type="receive"
					title="Sun* Inc"
					subtitle="Đã gửi tin nhắn cho bạn"
					time="5 giờ trước"
				></notify-card>
				<notify-card
					type="deny"
					title="Sun* Inc"
					subtitle="Đã từ chối hồ sơ của bạn"
					time="12 giờ trước"
				></notify-card>
				<notify-card
					type="suggest"
					title="Công việc"
					subtitle="Xem công việc mới phù hợp với bạn"
					time="2 ngày trước"
				></notify-card>
			</div>

			<!-- applied job  -->
			<div
				class="bg-white p-4 rounded-lg lg:basis-2/3 flex flex-col gap-4"
			>
				<h1
					class="mb-4 text-sm md:text-base lg:text-xl font-semibold text-sky-900"
				>
					Công việc đã ứng tuyển
				</h1>

				<applied-job
					v-for="apply in applied"
					:key="apply.id"
					:id="apply.id"
					:name="apply.name"
					:logo="apply.logo"
					:time="apply.time"
					:location="apply.location"
					:status="apply.status"
				></applied-job>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import StatisticCard from "../../components/dashboard/StatisticCard.vue";
import NotifyCard from "../../components/dashboard/NotifyCard.vue";
import AppliedJob from "../../components/dashboard/AppliedJob.vue";
export default {
	components: {
		StatisticCard,
		NotifyCard,
		AppliedJob,
	},
    props: ['userId'],
	data() {
		return {
			applied: [
				{
					id: 1,
					name: "Sun* Inc",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					location: "Cau Giay, Ha Noi",
					time: "23/10/2023",
					status: "Chấp nhận",
				},
				{
					id: 2,
					name: "Sun* Inc",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					location: "Cau Giay, Ha Noi",
					time: "23/10/2023",
					status: "Đang chờ",
				},
				{
					id: 3,
					name: "Sun* Inc",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					location: "Cau Giay, Ha Noi",
					time: "23/10/2023",
					status: "Từ chối",
				},
			],
		};
	},
    mounted() {
        console.log(this.userId);
        
    }
};
</script>
