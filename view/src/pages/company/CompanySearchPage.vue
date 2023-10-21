<template>
	<main class="pt-16 lg:pt-20 bg-gray-200">
		<div class="px-20 flex flex-col lg:flex-row gap-6 mt-10 pb-10">
			<!-- search engine -->
			<div
				class="basis-1/4 bg-white shadow-sm p-4 rounded-lg flex flex-col gap-6 h-min max-h-min"
			>
				<div class="flex justify-between">
					<h1
						class="text-xs md:text-sm lg:text-lg font-bold text-sky-950"
					>
						Tìm kiếm công ty
					</h1>
					<button
						class="text-xs md:text-sm lg:text-base text-slate-600"
						@click="refresh"
					>
						Xóa
					</button>
				</div>
				<div class="flex flex-col gap-3">
					<input
						type="text"
						placeholder="Tên công ty"
						class="border border-sky-900 px-4 py-3 rounded-md w-full outline-none focus:border-green-600"
						v-model="nameCompany"
					/>
					<input
						type="text"
						placeholder="Địa điểm"
						class="border border-sky-900 px-4 py-3 rounded-md w-full outline-none focus:border-green-600"
						v-model="workLocation"
					/>
				</div>

				<!-- Field  -->
				<div class="flex flex-col gap-4">
					<span class="flex items-center justify-between">
						<h1
							class="text-xs md:text-sm lg:text-base font-semibold"
						>
							Lĩnh vực
						</h1>
						<font-awesome-icon
							icon="fa-solid fa-chevron-up"
							class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer"
							v-if="!isExpandSkills"
							@click="expand('skills')"
						/>
						<font-awesome-icon
							icon="fa-solid fa-chevron-down"
							class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer"
							v-else
							@click="expand('skills')"
						/>
					</span>
					<transition name="detail">
						<ul
							class="flex flex-col gap-2 text-slate-600 text-xs md:text-sm lg:text-base"
							v-if="isExpandSkills"
						>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="web" />
								<label for="web">Phát triển web (102)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="app" />
								<label for="app"
									>Phát triển ứng dụng (46)</label
								>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="security" />
								<label for="security">Bảo mật (4)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="data" />
								<label for="data">Khoa học dữ liệu (20)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="cloud" />
								<label for="cloud"
									>Điện toán đám mây (20)</label
								>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="network" />
								<label for="network">Network (20)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="ai" />
								<label for="ai">Trí tuệ nhân tạo (20)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="rnd" />
								<label for="rnd">RnD (20)</label>
							</li>
						</ul>
					</transition>
				</div>

				<!-- Level  -->
				<div class="flex flex-col gap-4">
					<span class="flex items-center justify-between">
						<h1
							class="text-xs md:text-sm lg:text-base font-semibold"
						>
							Trình độ
						</h1>
						<font-awesome-icon
							icon="fa-solid fa-chevron-up"
							class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer"
							v-if="!isExpandLevel"
							@click="expand('level')"
						/>
						<font-awesome-icon
							icon="fa-solid fa-chevron-down"
							class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer"
							v-else
							@click="expand('level')"
						/>
					</span>
					<transition name="detail">
						<ul
							class="flex flex-col gap-2 text-slate-600 text-xs md:text-sm lg:text-base"
							v-if="isExpandLevel"
						>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="intern" />
								<label for="intern">Intern</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="junior" />
								<label for="junior">Junior</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="middle" />
								<label for="middle">Middle</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="senior" />
								<label for="senior">Senior</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="lead" />
								<label for="lead">Team Leader</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="manager" />
								<label for="manager">Manager</label>
							</li>
						</ul>
					</transition>
				</div>
				<button
					class="w-full bg-green-400 p-4 rounded-lg text-sky-900 font-bold hover:bg-green-500 hover:text-sky-800"
				>
					Tìm kiếm
				</button>
			</div>

			<div class="basis-3/4">
				<div
					class="flex justify-between items-center w-full text-xs lg:text-sm font-semibold text-sky-900"
				>
					<p>120 kết quả</p>
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
										class="px-4 py-2 relative bg-white text-gray-600 w-full rounded-t-md hover:bg-cyan-700 hover:text-white"
									>
										Tên
									</button>
								</li>
								<li>
									<button
										class="px-4 py-2 relative bg-white text-gray-600 w-full hover:bg-cyan-700 hover:text-white"
									>
										Tuyển gấp
									</button>
								</li>
								<li>
									<button
										class="px-4 py-2 relative bg-white text-gray-600 w-full rounded-b-md hover:bg-cyan-700 hover:text-white"
									>
										Ngày đăng
									</button>
								</li>
							</ul>
						</transition>
					</button>
				</div>
				<div
					class="flex justify-between items-center w-full text-xs lg:text-sm font-semibold text-sky-900"
				></div>

				<ul
					class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-4 mt-4"
				>
					<card-company
						v-for="company in companies"
						:id="company.id"
						:key="company.id"
						:companyName="company.companyName"
						:companyDescription="company.companyDescription"
						:companyAddress="company.companyAddress"
						:logo="company.logo"
					></card-company>
				</ul>

				<div
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
				</div>
			</div>
		</div>
	</main>
</template>

<script lang="ts">
import CardCompany from "../../components/company/CardCompany.vue";
export default {
	components: {
		CardCompany,
	},
	data() {
		return {
			experienceLevel: false,
			isExpandLocation: false,
			isExpandSkills: false,
			isExpandExperience: false,
			isExpandLevel: false,
			isExpandSort: false,
			nameCompany: "",
			workLocation: "",
			companies: [
				{
					id: 1,
					companyName: "Sun* INC Company",
					companyDescription: "Software and Consultancy",
					companyAddress: "Ha Noi, Viet Nam",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
				},
				{
					id: 2,
					companyName: "Sun* INC Company",
					companyDescription: "Software and Consultancy",
					companyAddress: "Ha Noi, Viet Nam",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-2.png",
				},

				{
					id: 3,
					companyName: "Sun* INC Company",
					companyDescription: "Software and Consultancy",
					companyAddress: "Ha Noi, Viet Nam",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-3.png",
				},
				{
					id: 4,
					companyName: "Sun* INC Company",
					companyDescription: "Software and Consultancy",
					companyAddress: "Ha Noi, Viet Nam",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-4.png",
				},
				{
					id: 5,
					companyName: "Sun* INC Company",
					companyDescription: "Software and Consultancy",
					companyAddress: "Ha Noi, Viet Nam",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-5.png",
				},
				{
					id: 6,
					companyName: "Sun* INC Company",
					companyDescription: "Software and Consultancy",
					companyAddress: "Ha Noi, Viet Nam",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-6.png",
				},
				{
					id: 7,
					companyName: "Sun* INC Company",
					companyDescription: "Software and Consultancy",
					companyAddress: "Ha Noi, Viet Nam",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-7.png",
				},
				{
					id: 8,
					companyName: "Sun* INC Company",
					companyDescription: "Software and Consultancy",
					companyAddress: "Ha Noi, Viet Nam",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-8.png",
				},
				{
					id: 9,
					companyName: "Sun* INC Company",
					companyDescription: "Software and Consultancy",
					companyAddress: "Ha Noi, Viet Nam",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-9.png",
				},
			],
		};
	},
	methods: {
		expand(type: String) {
			switch (type) {
				case "category":
					this.experienceLevel = !this.experienceLevel;
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
			this.experienceLevel = false;
			this.isExpandLocation = false;
			this.isExpandSkills = false;
			this.isExpandExperience = false;
			this.isExpandLevel = false;
			this.nameCompany = "";
			this.workLocation = "";
		},
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
