<template>
	<main class="pt-16 lg:pt-20 w-full h-auto">
		<!-- job header  -->
		<div class="px-10 xl:px-40 pt-20 pb-10 bg-amber-50">
			<div class="flex flex-col md:flex-row gap-6">
				<span class="flex flex-col gap-4 items-center">
					<span class="flex flex-col items-center gap-2">
						<img
							:src="current_job.company_logo"
							alt="company logo"
							class="w-28 h-auto"
						/>
						<p
							class="font-bold text-xs md:text-sm lg:text-base text-sky-900"
						>
							{{ current_job.company_name }}
						</p>
					</span>
					<p
						class="px-3 py-1 bg-orange-400 rounded-lg text-xs lg:text-sm text-white"
					>
						Đang tuyển {{ current_job.quantity }} vị trí
					</p>
				</span>

				<div class="flex flex-col gap-8">
					<div class="flex flex-col gap-2">
						<span
							class="bg-green-200 px-3 py-1 rounded-lg text-green-700 font-semibold text-xs lg:text-sm max-w-max"
							>{{ current_job.level }}</span
						>
						<h1
							class="text-xl md:text-2xl lg:text-3xl font-bold text-sky-900"
						>
							{{ current_job.role }}
						</h1>
						<span
							class="flex items-center gap-1 text-xs lg:text-sm text-sky-900"
						>
							<font-awesome-icon
								icon="fa-solid fa-location-dot"
							/>
							<address>
								{{ current_job.address }}
							</address>
						</span>
					</div>

					<div class="flex flex-col gap-2">
						<h2
							class="text-xs md:text-sm lg:text-base font-bold text-red-500"
						>
							Lương: {{ current_job.salary }}
						</h2>
					</div>

					<p class="text-sm italic text-gray-700">
						Ngày hết hạn: {{ current_job.deadline }}
					</p>
				</div>
			</div>
		</div>

		<!-- job description and suggest job -->
		<div class="px-10 xl:px-40 pt-4 pb-10 flex flex-col lg:flex-row gap-10">
			<div
				class="p-4 border border-green-400 rounded-lg flex flex-col justify-between gap-6 lg:basis-2/3 h-min"
			>
				<div class="flex flex-col gap-6">
					<ul class="flex gap-6 text-xs md:text-sm lg:text-base">
						<li
							class="px-8 py-1 bg-green-600 text-white rounded-xl hover:cursor-pointer hover:bg-green-700"
							@click="show('description')"
						>
							Mô tả
						</li>
						<li
							class="px-8 py-1 bg-green-600 text-white rounded-xl hover:cursor-pointer hover:bg-green-700"
							@click="show('requirement')"
						>
							Yêu cầu
						</li>
						<li
							class="px-8 py-1 bg-green-600 text-white rounded-xl hover:cursor-pointer hover:bg-green-700"
							@click="show('benefit')"
						>
							Quyền lợi
						</li>
					</ul>

					<!-- Job description paragraph  -->
					<transition name="detail">
						<div
							class="flex flex-col gap-4 text-xs md:text-sm lg:text-base text-sky-950"
							v-if="isShowDescription"
						>
							<p
								class="leading-7"
								v-for="desc in current_job.description"
							>
								{{ desc }}
							</p>
						</div>
					</transition>

					<!-- Yêu cầu  -->
					<transition name="detail">
						<div
							class="flex flex-col gap-4 text-xs md:text-sm lg:text-base"
							v-if="isShowRequirement"
						>
							<!-- Yêu cầu công việc  -->
							<span class="flex flex-col gap-3">
								<h1
									class="text-sm md:text-base lg:text-xl font-bold"
								>
									Yêu cầu:
								</h1>
								<ul
									class="text-xs md:text-sm lg:text-base flex flex-col gap-2"
								>
									<li
										class="flex items-center gap-2"
										v-for="require in current_job.demand
											.require"
									>
										<font-awesome-icon
											icon="fa-regular fa-circle-dot"
										/>
										<p>
											{{ require }}
										</p>
									</li>
								</ul>
							</span>

							<!-- Công việc cần làm  -->
							<span class="flex flex-col gap-3">
								<h1
									class="text-sm md:text-base lg:text-xl font-bold"
								>
									Công việc:
								</h1>
								<ul
									class="text-xs md:text-sm lg:text-base flex flex-col gap-2"
								>
									<li
										class="flex items-center gap-2"
										v-for="job in current_job.demand.job"
									>
										<font-awesome-icon
											icon="fa-regular fa-circle-dot"
										/>
										<p>
											{{ job }}
										</p>
									</li>
								</ul>
							</span>

							<!-- Bằng cấp và kĩ năng  -->
							<span class="flex flex-col gap-3">
								<h1
									class="text-sm md:text-base lg:text-xl font-bold"
								>
									Bằng cấp và kĩ năng:
								</h1>
								<ul
									class="text-xs md:text-sm lg:text-base flex flex-col gap-2"
								>
									<li
										class="flex items-center gap-2"
										v-for="skill in current_job.demand
											.degree_skill"
									>
										<font-awesome-icon
											icon="fa-regular fa-circle-dot"
										/>
										<p>
											{{ skill }}
										</p>
									</li>
								</ul>
							</span>
						</div>
					</transition>

					<!-- Quyền lợi  -->
					<transition name="detail">
						<div
							class="flex flex-col gap-4 text-xs md:text-sm lg:text-base"
							v-if="isShowBenefit"
						>
							<ul
								class="text-xs md:text-sm lg:text-base flex flex-col gap-2"
							>
								<li
									class="flex items-center gap-2"
									v-for="benefit in current_job.benefit"
								>
									<font-awesome-icon
										icon="fa-regular fa-circle-dot"
									/>
									<p>
										{{ benefit }}
									</p>
								</li>
							</ul>
						</div>
					</transition>
				</div>

				<div class="flex gap-4 text-xs md:text-sm lg:text-base">
					<button
						class="bg-green-300 px-4 py-2 rounded-lg font-bold text-sky-900 hover:bg-green-400 hover:cursor-pointer"
						@click="showApply"
					>
						Ứng tuyển ngay
					</button>
					<button
						class="border border-green-300 px-4 py-2 rounded-lg text-sky-900 font-semibold hover:cursor-pointer hover:border-green-500"
					>
						Lưu tin
					</button>
				</div>
			</div>

			<div class="flex flex-col gap-4 lg:basis-1/3">
				<h1
					class="text-base md:text-lg lg:text-xl font-bold text-sky-900 mb-4"
				>
					Việc làm tương tự
				</h1>

				<ul class="flex flex-col gap-4">
					<job-card
						v-for="job in jobs"
						:key="job.id"
						:id="job.id"
						:featured="job.featured"
						:urgent="job.urgent"
						:level="job.level"
						:company_logo="job.company_logo"
						:role="job.role"
						:company_name="job.company_name"
						:salary="job.salary"
						:quantity="job.quantity"
					></job-card>
				</ul>

				<router-link
					to="/jobsearch"
					class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800 w-full text-center"
					>Xem thêm</router-link
				>
			</div>
		</div>

		<!-- job application form  -->
		<base-form :show="!!isShowApply" @close="closeApply"></base-form>
	</main>
</template>

<script lang="ts">
import BaseForm from "../../components/ui/BaseForm.vue";
export default {
	components: {
		BaseForm,
	},
	// props nhận được khi click từ một job card
	props: ["id"],
	data() {
		return {
			isShowDescription: true,
			isShowRequirement: false,
			isShowBenefit: false,
			isShowApply: false,
			jobs: [
				{
					id: 1,
					featured: true,
					urgent: true,
					level: "Senior",
					role: "Jr. PHP Developer",
					company_name: "ABC Company",
					company_logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					salary: "$5K - $8K",
					quantity: "6",
				},
				{
					id: 2,
					featured: true,
					urgent: true,
					level: "Junior",
					role: "Frontend Developer",
					company_name: "SBC Company",
					company_logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-2.png",
					salary: "$3K - $5K",
					quantity: "3",
				},
			],
			current_job: {
				level: "",
				role: "",
				demand: {
					require: [],
					job: [],
					degree_skill: [],
				},
				salary: "",
				benefit: [],
				urgent: null,
				company_name: "",
				company_logo: "",
				quantity: "",
				address: "",
				description: [],
				posting_date: "",
				deadline: "",
			},
		};
	},
	methods: {
		show(type: String) {
			switch (type) {
				case "description":
					this.isShowDescription = true;
					this.isShowRequirement = false;
					this.isShowBenefit = false;
					break;
				case "requirement":
					this.isShowDescription = false;
					this.isShowRequirement = true;
					this.isShowBenefit = false;
					break;
				case "benefit":
					this.isShowDescription = false;
					this.isShowRequirement = false;
					this.isShowBenefit = true;
					break;
			}
		},
		showApply() {
			this.isShowApply = true;
		},
		closeApply() {
			this.isShowApply = false;
		},
		async getJob(id: String) {
			// call api to get job detail
			try {
				this.current_job = await this.$store.dispatch(
					"jobs/getJob",
					id
				);
			} catch (err) {
				console.log(err);
			}
		},
	},
	mounted() {
		this.getJob(this.id);
	},
};
</script>

<style scoped>
.detail-enter-from {
	opacity: 0;
	transform: translateY(-30px);
}

.detail-enter-to {
	opacity: 1;
	transform: translateY(0);
}

.detail-enter-active {
	transition: all 0.3s ease-out;
}
</style>
