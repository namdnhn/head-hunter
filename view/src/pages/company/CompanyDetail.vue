<template>
	<main class="pt-16 lg:pt-20 w-full h-auto">
		<!-- job header  -->
		<div class="px-10 xl:px-40 pt-20 pb-10 bg-amber-50">
			<div class="flex flex-col md:flex-row gap-10">
				<!-- anh vs ten -->
				<span class="flex flex-col gap-4 items-center">
					<span class="flex flex-col items-center gap-4">
						<img
							src="https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-12.png"
							alt="company logo"
							class="w-28 h-auto"
						/>
						<p
							class="font-bold text-sm md:text-base lg:text-xl text-sky-900"
						>
							Sun* Inc Company
						</p>
						<p
							class="px-3 py-1 bg-orange-400 rounded-lg text-xs lg:text-sm text-white"
						>
							Đang tuyển 4 công việc
						</p>
					</span>
				</span>

				<div class="flex flex-col items-start  justify-between gap-4">
					<div class="flex flex-col gap-2">
						<h1
							class="text-xl md:text-2xl lg:text-3xl font-bold text-sky-900"
						>
							Software and Consultancy
						</h1>
						<span
							class="flex items-center gap-1 text-xs lg:text-base text-sky-900"
						>
							<font-awesome-icon
								icon="fa-solid fa-location-dot"
							/>
							<address>Cầu Giấy, Hà Nội</address>
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
								1990
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
								800+
							</p>
						</div>
					</div>

					<button
						class="border border-red-500 bg-white px-4 py-2 rounded-3xl flex gap-2 items-center text-red-500 font-semibold"
					>
                    <font-awesome-icon icon="fa-regular fa-heart" class="text-red-500"/>Theo dõi
					</button>
				</div>
			</div>
		</div>

		<!-- job description and suggest job -->
		<div class="px-10 xl:px-40 pt-4 pb-10 flex flex-col lg:flex-row gap-10">
			<div
				class="p-4 border border-green-400 rounded-lg flex flex-col justify-between gap-6 lg:basis-2/3"
			>
				<div class="flex flex-col gap-6">
					<ul class="flex gap-6 text-xs md:text-sm lg:text-base">
						<li
							class="px-8 py-1 bg-green-600 text-white rounded-xl hover:cursor-pointer hover:bg-green-700"
							@click="show('description')"
						>
							Mô tả
						</li>
						<!-- <li class="px-8 py-1 bg-green-600 text-white rounded-xl hover:cursor-pointer hover:bg-green-700"
                            @click="show('requirement')">
                            Yêu cầu
                        </li>
                        <li class="px-8 py-1 bg-green-600 text-white rounded-xl hover:cursor-pointer hover:bg-green-700"
                            @click="show('benefit')">
                            Quyền lợi
                        </li> -->
					</ul>

					<!-- Job description paragraph  -->
					<transition name="detail">
						<div
							class="flex flex-col gap-4 text-xs md:text-sm lg:text-base text-sky-950"
							v-if="isShowDescription"
						>
							<p class="leading-7">
								Công ty phần mềm đóng một vai trò quan trọng
								trong cuộc cách mạng công nghệ thông tin và làm
								thay đổi cách chúng ta làm việc và tương tác với
								thế giới xung quanh. Một trong những công ty
								tiên phong và nổi tiếng trong lĩnh vực này chính
								là Công ty ABC - một nơi nơi sự sáng tạo và khám
								phá không giới hạn được biến thành các sản phẩm
								phần mềm xuất sắc. <br />

								Với hơn 20 năm kinh nghiệm trong ngành công
								nghệ, Công ty ABC đã trở thành một địa chỉ đáng
								tin cậy cho những dự án phần mềm độc đáo và tùy
								chỉnh. Chúng tôi tự hào về đội ngũ những chuyên
								gia phần mềm tài năng, luôn sáng tạo và nắm bắt
								những cơ hội mới nhất trong ngành. Điều này giúp
								chúng tôi không ngừng phát triển và mang đến
								những sản phẩm phần mềm đỉnh cao cho khách hàng
								của mình. <br />

								Công ty ABC chuyên sâu trong việc phát triển
								phần mềm cho nhiều lĩnh vực, bao gồm ứng dụng di
								động, ứng dụng web, phần mềm doanh nghiệp, trí
								tuệ nhân tạo và nhiều lĩnh vực công nghệ khác.
								Chúng tôi không chỉ cung cấp các giải pháp phần
								mềm tùy chỉnh mà còn phát triển và duy trì các
								sản phẩm phần mềm tiêu chuẩn cao với tầm ảnh
								hưởng toàn cầu. <br />

								Một trong những giá trị cốt lõi của Công ty ABC
								là cam kết về chất lượng. Chúng tôi luôn tuân
								thủ các quy trình kiểm tra chất lượng nghiêm
								ngặt để đảm bảo rằng sản phẩm của mình hoạt động
								tốt, an toàn và đáng tin cậy. Chúng tôi luôn
								lắng nghe ý kiến của khách hàng và sẵn sàng điều
								chỉnh sản phẩm để đáp ứng nhu cầu cụ thể của họ.
								<br />

								Bên cạnh việc phát triển phần mềm, Công ty ABC
								cũng nỗ lực không ngừng trong việc nghiên cứu và
								phát triển công nghệ mới. Chúng tôi luôn ứng
								dụng các công nghệ tiên tiến như trí tuệ nhân
								tạo, học máy và blockchain để mang đến những
								giải pháp sáng tạo và tương lai cho khách hàng.
								<br />

								Công ty ABC tự hào là đối tác đáng tin cậy của
								nhiều doanh nghiệp lớn trên khắp thế giới và
								luôn sẵn sàng hỗ trợ họ trong việc tận dụng sức
								mạnh của công nghệ thông tin. Với cam kết về
								chất lượng, sáng tạo và sự phục vụ tận tâm,
								chúng tôi hy vọng có thể tiếp tục đồng hành và
								cùng bạn xây dựng những sản phẩm phần mềm xuất
								sắc trong tương lai. <br />
							</p>
						</div>
					</transition>
				</div>

				<div class="flex gap-4 text-xs md:text-sm lg:text-base">
					<button
						class="bg-green-300 px-4 py-2 rounded-lg font-bold text-sky-900 hover:bg-green-400 hover:cursor-pointer"
					>
						Xem các công việc hiện có
					</button>
					<button
						class="border border-green-300 px-4 py-2 rounded-lg text-sky-900 font-semibold hover:cursor-pointer hover:border-green-500"
					>
						Lưu công ty
					</button>
				</div>
			</div>

			<div class="flex flex-col gap-4 lg:basis-1/3">
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
						:logo="job.logo"
						:job="job.job"
						:desc="job.desc"
						:salary="job.salary"
						:position="job.position"
					></job-card>
				</ul>
				<button
					type="button"
					class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
				>
					Xem thêm
				</button>
			</div>
		</div>
	</main>
</template>

<script lang="ts">
export default {
	// props nhận được khi click từ một job card
	props: [
		"id",
		"featured",
		"urgent",
		"level",
		"logo",
		"job",
		"desc",
		"salary",
		"position",
	],
	data() {
		return {
			isShowDescription: true,
			isShowRequirement: false,
			isShowBenefit: false,
			jobs: [
				{
					id: 1,
					featured: true,
					urgent: true,
					level: "Senior",
					job: "Jr. PHP Developer",
					desc: "CSS3, HTML5, Javascript, Bootstrap, Jquery",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
					salary: "$5K - $8K",
					position: "6",
				},
				{
					id: 2,
					featured: true,
					urgent: true,
					level: "Junior",
					job: "Frontend Developer",
					desc: "React, Vue, Angular, CSS, HTML, Javascript",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-2.png",
					salary: "$3K - $5K",
					position: "3",
				},
			],
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
