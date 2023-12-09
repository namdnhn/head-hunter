<template>
	<main class="pt-16 lg:pt-20 bg-gray-200">
		<div class="px-20 flex flex-col lg:flex-row gap-6 mt-10 pb-10">
			<div class="w-full">
				<div
					class="flex justify-between items-center w-full text-xs lg:text-sm font-semibold text-sky-900"
				>
					<p>{{ jobs.length }} kết quả</p>
					<button
						class="px-4 py-2 relative bg-white rounded-md text-gray-600 flex justify-between items-center gap-2"
						@click="expand('sort')"
					>
						<p>Sắp xếp</p>
						<font-awesome-icon
							icon="fa-solid fa-chevron-up"
							v-if="!isExpandSort"
						/>
						<font-awesome-icon
							icon="fa-solid fa-chevron-down"
							v-else
						/>
						<transition name="detail">
							<ul
								class="absolute top-full left-0 right-0 mt-1 shadow-md"
								v-if="isExpandSort"
							>
								<li>
									<button
										class="px-4 py-2 relative bg-white text-gray-600 w-full rounded-t-md hover:bg-green-400 hover:text-white"
									>
										Tên
									</button>
								</li>
								<li>
									<button
										class="px-4 py-2 relative bg-white text-gray-600 w-full hover:bg-green-400 hover:text-white"
									>
										Tuyển gấp
									</button>
								</li>
								<li>
									<button
										class="px-4 py-2 relative bg-white text-gray-600 w-full rounded-b-md hover:bg-green-400 hover:text-white"
									>
										Ngày đăng
									</button>
								</li>
							</ul>
						</transition>
					</button>
				</div>

				<ul
					class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-4 mt-4"
				>
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

				<!-- <div
					class="mt-4 flex items-center justify-center gap-6 text-xs md:text-sm lg:text-base"
				>
					<font-awesome-icon
						icon="fa-solid fa-angles-left"
						class="p-2 hover:cursor-pointer hover:bg-green-300 rounded-md"
					/>
					<span
						class="py-2 px-4 hover:cursor-pointer hover:bg-green-300 rounded-md"
						>1</span
					>
					<span
						class="py-2 px-4 hover:cursor-pointer hover:bg-green-300 rounded-md"
						>2</span
					>
					<span
						class="py-2 px-4 hover:cursor-pointer hover:bg-green-300 rounded-md"
						>3</span
					>
					<span
						class="py-2 px-4 hover:cursor-pointer hover:bg-green-300 rounded-md"
						>4</span
					>
					<font-awesome-icon
						icon="fa-solid fa-angles-right"
						class="p-2 hover:cursor-pointer hover:bg-green-300 rounded-md"
					/>
				</div> -->
			</div>
		</div>
	</main>
</template>

<script lang="ts">
export default {
	props: ["id"],
	data() {
		return {
			isExpandCategory: false,
			isExpandLocation: false,
			isExpandSkills: false,
			isExpandExperience: false,
			isExpandLevel: false,
			isExpandSort: false,
			jobPosition: "",
			workLocation: "",
			jobs: [],
		};
	},
	methods: {
		expand(type: String) {
			switch (type) {
				case "category":
					this.isExpandCategory = !this.isExpandCategory;
					break;
				case "location":
					this.isExpandLocation = !this.isExpandLocation;
					break;
				case "skills":
					this.isExpandSkills = !this.isExpandSkills;
					break;
				case "experience":
					this.isExpandExperience = !this.isExpandExperience;
					break;
				case "level":
					this.isExpandLevel = !this.isExpandLevel;
					break;
				case "sort":
					this.isExpandSort = !this.isExpandSort;
					break;
			}
		},
		refresh() {
			this.isExpandCategory = false;
			this.isExpandLocation = false;
			this.isExpandSkills = false;
			this.isExpandExperience = false;
			this.isExpandLevel = false;
			this.jobPosition = "";
			this.workLocation = "";
		},
		async getJobs() {
			// call api to get jobs
			try {
				this.isLoading = true;
				const res = await fetch(
					`http://localhost:8000/api/job/company/${this.id}`,
					{
						method: "GET",
						headers: {
							"Content-Type": "application/json",
						},
					}
				);

				const responseData = await res.json();

				console.log(responseData);
				this.jobs = responseData;
			} catch (err) {
				console.log(err);
			}
		},
	},
	mounted() {
		this.getJobs();
	},
};
</script>

<style scoped>
.detail-enter-from {
	opacity: 0;
	transform: translateY(-30px);
}

.detail-leave-to {
	opacity: 0;
	transform: translateY(30px);
}

.detail-enter-to,
.detail-leave-from {
	opacity: 1;
	transform: translateY(0);
}

.detail-enter-active {
	transition: all 0.3s ease-out;
}

.detail-leave-active {
	transition: all 0.3s ease-in;
}
</style>
