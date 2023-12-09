<template>
	<main class="pt-16 lg:pt-20 h-auto w-full">
		<!-- company header  -->
		<div class="px-10 xl:px-40 pt-20 pb-10 bg-amber-50">
			<div class="flex flex-col md:flex-row gap-10">
				<!-- anh vs ten -->
				<span class="flex flex-col gap-4 items-center">
					<span class="flex flex-col items-center gap-4">
						<img
							:src="company_info.logo"
							alt="company logo"
							class="h-28 w-28 rounded-full"
						/>
						<p
							class="px-3 py-1 bg-orange-400 rounded-lg text-xs lg:text-sm text-white"
						>
							Đang tuyển {{ company_info.job_quantity }} công
							việc
						</p>
					</span>
				</span>

				<div class="flex flex-col items-start justify-between gap-4">
					<div class="flex flex-col gap-2">
						<h1
							class="text-xl md:text-2xl lg:text-3xl font-bold text-sky-900"
						>
							{{ company_info.name }}
						</h1>
						<span
							class="flex items-center gap-1 text-xs lg:text-base text-sky-900"
						>
							<font-awesome-icon
								icon="fa-solid fa-location-dot"
							/>
							<address>{{ company_info.address }}</address>
						</span>
					</div>
					<div class="flex gap-16">
						<div>
							<label
								class="text-base md:text-lg lg:text-xl font-medium"
								>Năm thành lập</label
							>
							<p
								class="text-sm md:text-base lg:text-lg font-semibold text-sky-900"
							>
								{{ company_info.founded_year }}
							</p>
						</div>
						<div>
							<label
								class="text-base md:text-lg lg:text-xl font-medium"
								>Số lượng nhân viên</label
							>
							<p
								class="text-sm md:text-base lg:text-lg font-semibold text-sky-900"
							>
								{{ company_info.employee_quantity }}
							</p>
						</div>
					</div>

					<button
						class="border border-red-500 bg-white px-4 py-2 rounded-3xl flex gap-2 items-center text-red-500 font-semibold"
					>
						<font-awesome-icon
							icon="fa-regular fa-heart"
							class="text-red-500"
						/>Theo dõi
					</button>
				</div>
			</div>
		</div>

		<!-- Detail info and suggest jobs  -->
		<div
			class="px-10 lg:px-20 xl:px-40 py-10 flex flex-col lg:flex-row lg:gap-10"
		>
			<!-- User info  -->
			<div class="w-full">
				<!-- introduce  -->
				<div
					class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10"
				>
					<span class="flex justify-between">
						<h1
							class="text-base md:text-lg lg:text-xl font-bold text-sky-900"
						>
							Giới thiệu
						</h1>
					</span>

					<!-- Paragraph  -->
					<p
						class="text-xs md:text-sm lg:text-base text-gray-600"
					>
						{{ company_info.description }}
					</p>
                    
					<div class="flex gap-4 text-xs md:text-sm lg:text-base">
						<router-link
							:to="jobsearch"
							class="bg-green-300 px-4 py-2 rounded-lg font-bold text-sky-900 hover:bg-green-400 hover:cursor-pointer"
						>
							Xem các công việc hiện có
						</router-link>
						<router-link
							class="border border-green-300 px-4 py-2 rounded-lg text-sky-900 font-semibold hover:cursor-pointer hover:border-green-500"
							:to="recruitmentLink"
                            v-if="isCompany"
						>
							Tạo tin tuyển dụng mới
						</router-link>
					</div>
				</div>
			</div>

			<!-- công việc đang tuyển dụng  -->
			<!-- <div class="flex flex-col gap-4 lg:basis-1/3">
				<h1
					class="text-base md:text-lg lg:text-xl font-bold text-sky-900 mb-4"
				>
					Công việc đang tuyển dụng
				</h1>

				<ul class="flex flex-col gap-4">
					<job-card
						v-for="job in jobs"
						:key="job.id"
						:id="job.id"
						:featured="job.featured"
						:urgent="job.urgent"
						:level="job.level"
						:job="job.job"
						:company_name="job.company_name"
						:company_logo="job.company_logo"
						:salary="job.salary"
						:role="job.role"
						:quantity="job.quantity"
					/>
				</ul>
				<router-link
					to="/companysearch"
					type="button"
					class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800 text-center"
				>
					Xem thêm
				</router-link>
			</div> -->
		</div>
	</main>
</template>

<script lang="ts">
export default {
	props: ["id"],
	data() {
		return {
			jobs: [
				{
					id: 1,
					featured: true,
					urgent: true,
					level: "Senior",
					role: "Jr. PHP Developer",
					company_name: "ABC Company",
					company_logo:
						"https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
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
					company_logo:
						"https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-2.png",
					salary: "$3K - $5K",
					quantity: "3",
				},
			],
			introduce:
				"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
			isEdittingIntroduce: false,
			current_company: [
				{
					id: "",
					logo: "",
					name: "",
					address: "",
					founded_year: "",
					employee_quantity: "",
					description: [],
					contact: "",
					job_quantity: "",
				},
			],
			isLoading: false,
			company_info: {
				address: "",
				contact: "",
				description: "",
				employee_quantity: 0,
				founded_year: 0,
				id: 0,
				job_quantity: 0,
				logo: "",
				name: "",
				user_id: 0,
			},
		};
	},
	methods: {
		editIntroduce() {
			this.isEdittingIntroduce = true;
		},
		saveIntroduce() {
			this.isEdittingIntroduce = false;
		},
		async getCompanyInfo() {
			try {
				this.isLoading = true;
				const res = await fetch(
					`http://localhost:8000/api/company/${this.id}`,
					{
						method: "GET",
						headers: {
							"Content-Type": "application/json",
						},
					}
				);

				const responseData = await res.json();
				this.company_info = responseData;
				console.log(this.company_info);
			} catch (error) {
				console.log(error);
			}
			this.isLoading = false;
		},
	},
	mounted() {
		this.getCompanyInfo();
	},
	computed: {
		recruitmentLink() {
			return `/companyprofile/${
				this.$route.params.id || this.id
			}/recruitmentpost`;
		},
		jobsearch() {
			return `/jobsearch`;
		},
        isCompany() {
			return this.$store.getters.isCompany;
		},
	},
    watch: {
        isCompany() {
			this.getCompanyInfo();
		},
    }
};
</script>
