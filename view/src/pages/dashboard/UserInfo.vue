<template>
	<div class="p-8 md:basis-3/5 lg:basis-4/5 flex flex-col gap-10">
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
					:position="apply.role"
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
	data() {
		return {
			applied: [],
			listApp: [],
		};
	},
	methods: {
		async getListApplied() {
			const userId = localStorage.getItem("userId");
			const res = await fetch(
				`https://head-hunter-b9ee2-default-rtdb.asia-southeast1.firebasedatabase.app/applied.json?orderBy="user_id"&equalTo="${userId}"`
			);

			const responseData = await res.json();

			for (const key in responseData) {
				this.listApp.push({
					job_id: responseData[key].job_id,
					job_status: responseData[key].job_status,
				});
			}
		},

		async getJobApplied() {
			for (const key in this.listApp) {
				const res = await fetch(
					"http://localhost:8000/api/job/" + this.listApp[key].job_id
				);
				const responseData = await res.json();
				console.log(responseData);
				let status = "";
				if (this.listApp[key].job_status == "pending") {
					status = "Đang chờ";
				} else if (this.listApp[key].job_status === "approved") {
					status = "Đã chấp nhận";
				} else if (this.listApp[key].job_status === "denied") {
					status = "Đã từ chối";
				}
				this.applied.push({
                    id: this.listApp[key].job_id,
					name: responseData.company_name,
					logo: responseData.company_logo,
					role: responseData.role,
					status: status,
				});
			}
		},
	},
	async mounted() {
		await this.getListApplied();
		await this.getJobApplied();
	},
};
</script>
