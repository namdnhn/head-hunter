<template>
	<main class="pt-16 lg:pt-20 bg-gray-200">
		<div class="px-20 flex flex-col lg:flex-row gap-6 mt-10">
			<!-- search engine -->
			<div
				class="basis-1/4 bg-white shadow-sm p-4 rounded-lg flex flex-col gap-6"
			>
				<div class="flex justify-between">
					<h1
						class="text-xs md:text-sm lg:text-lg font-bold text-sky-950"
					>
						Tìm kiếm công việc
					</h1>
					<button
						class="text-xs md:text-sm lg:text-base text-slate-600"
					>
						Xóa
					</button>
				</div>
				<div class="flex flex-col gap-3">
					<input
						type="text"
						placeholder="Vị trí tuyển dụng"
						class="border border-sky-900 px-4 py-3 rounded-md w-full outline-none focus:border-green-600"
					/>
					<input
						type="text"
						placeholder="Địa điểm"
						class="border border-sky-900 px-4 py-3 rounded-md w-full outline-none focus:border-green-600"
					/>
				</div>

				<!-- Category  -->
				<div class="flex flex-col gap-4">
					<span class="flex items-center justify-between">
						<h1
							class="text-xs md:text-sm lg:text-base font-semibold"
						>
							Thể loại
						</h1>
						<font-awesome-icon
							icon="fa-solid fa-chevron-up"
							class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer"
							v-if="!isExpandCategory"
							@click="expand('category')"
						/>
						<font-awesome-icon
							icon="fa-solid fa-chevron-down"
							class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer"
							v-else
							@click="expand('category')"
						/>
					</span>
					<transition name="detail">
						<ul
							class="flex flex-col gap-2 text-slate-600 text-xs md:text-sm lg:text-base"
							v-if="isExpandCategory"
						>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="frontend" />
								<label for="frontend">Frontend (31)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="backend" />
								<label for="backend">Backend (20)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="security" />
								<label for="security">Security (4)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="AI" />
								<label for="AI">AI (20)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="data" />
								<label for="data">Data Engineer (12)</label>
							</li>
						</ul>
					</transition>
				</div>

				<!-- Location  -->
				<div class="flex flex-col gap-4">
					<span class="flex items-center justify-between">
						<h1
							class="text-xs md:text-sm lg:text-base font-semibold"
						>
							Địa điểm làm việc
						</h1>
						<font-awesome-icon
							icon="fa-solid fa-chevron-up"
							class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer"
							v-if="!isExpandLocation"
							@click="expand('location')"
						/>
						<font-awesome-icon
							icon="fa-solid fa-chevron-down"
							class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer"
							v-else
							@click="expand('location')"
						/>
					</span>
					<transition name="detail">
						<ul
							class="flex flex-col gap-2 text-slate-600 text-xs md:text-sm lg:text-base"
							v-if="isExpandLocation"
						>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="hanoi" />
								<label for="hanoi">Hà Nội (31)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="danang" />
								<label for="danang">Đà nẵng (20)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="hcm" />
								<label for="hcm">TP. Hồ Chí Minh (4)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="nhatrang" />
								<label for="nhatrang">Nha Trang (20)</label>
							</li>
						</ul>
					</transition>
				</div>

				<!-- Skills  -->
				<div class="flex flex-col gap-4">
					<span class="flex items-center justify-between">
						<h1
							class="text-xs md:text-sm lg:text-base font-semibold"
						>
							Kỹ năng
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
								<input type="checkbox" id="html" />
								<label for="html"
									>HTML, CSS, Javascript (102)</label
								>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="vue" />
								<label for="vue">VueJS (46)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="node" />
								<label for="node">NodeJS (4)</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="react" />
								<label for="react">ReactJS (20)</label>
							</li>
						</ul>
					</transition>
				</div>

				<!-- Experience  -->
				<div class="flex flex-col gap-4">
					<span class="flex items-center justify-between">
						<h1
							class="text-xs md:text-sm lg:text-base font-semibold"
						>
							Kinh nghiệm
						</h1>
						<font-awesome-icon
							icon="fa-solid fa-chevron-up"
							class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer"
							v-if="!isExpandExperience"
							@click="expand('experience')"
						/>
						<font-awesome-icon
							icon="fa-solid fa-chevron-down"
							class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer"
							v-else
							@click="expand('experience')"
						/>
					</span>
					<transition name="detail">
						<ul
							class="flex flex-col gap-2 text-slate-600 text-xs md:text-sm lg:text-base"
							v-if="isExpandExperience"
						>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="less1" />
								<label for="less1">Dưới 1 năm</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="1year" />
								<label for="1year">1 năm</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="2year" />
								<label for="2year">2 năm</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="3year" />
								<label for="3year">3 năm</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="4year" />
								<label for="4year">4 năm</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="5year" />
								<label for="5year">5 năm</label>
							</li>
							<li class="flex gap-2 items-center">
								<input type="checkbox" id="more5" />
								<label for="more">Trên 5 năm</label>
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
				<div class="flex justify-between items-center w-full text-xs lg:text-sm font-semibold text-sky-900">
                    <p>Hiển thị 1 - 10 từ 20 kết quả</p>
					<button
						class="px-4 py-2 relative bg-white rounded-md text-gray-600 flex justify-between items-center gap-2"
                        @click="expand('sort')"
					>
						<p>Sắp xếp</p>
						<font-awesome-icon icon="fa-solid fa-chevron-up" v-if="!isExpandSort"/>
						<font-awesome-icon icon="fa-solid fa-chevron-down" v-else/>
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
			</div>
		</div>
	</main>
</template>

<script lang="ts">
export default {
	data() {
		return {
			isExpandCategory: false,
			isExpandLocation: false,
			isExpandSkills: false,
			isExpandExperience: false,
			isExpandLevel: false,
			isExpandSort: false,
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
