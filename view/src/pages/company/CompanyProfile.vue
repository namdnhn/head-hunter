<template>
	<main class="pt-16 lg:pt-20 h-auto w-full">
		<!-- company header  -->
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

				<div class="flex flex-col items-start justify-between gap-4">
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
			<div class="lg:basis-2/3">
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

						<!-- click to edit  -->
						<font-awesome-icon
							icon="fa-solid fa-pen-to-square"
							class="text-xs md:text-sm lg:text-base text-green-700 hover:cursor-pointer"
							@click="editIntroduce"
						/>
					</span>

					<!-- Paragraph  -->
					<p
						class="text-xs md:text-sm lg:text-base text-gray-600"
						v-if="!isEdittingIntroduce"
					>
						GIỚI THIỆU CÔNG TY: Techcombank mang sứ mệnh dẫn dắt
						hành trình số hóa của ngành tài chính, tạo động lực cho
						mỗi cá nhân, doanh nghiệp và tổ chức phát triển bền vững
						và bứt phá thành công. Được thành lập vào tháng 9 năm
						1993 và có trụ sở chính tại Hà Nội, Techcombank là một
						trong những ngân hàng thương mại cổ phần lớn nhất tại
						Việt Nam và là một trong những tổ chức ngân hàng hàng
						đầu tại Châu Á. Chúng tôi có hơn 12.000 nhân viên và 9.6
						triệu khách hàng bán lẻ và khách hàng doanh nghiệp tại
						Việt Nam. Mạng lưới rộng khắp của chúng tôi gồm 309 chi
						nhánh và phòng giao dịch trên 45 tỉnh thành. Techcombank
						là ngân hàng thương mại tư nhân đầu tiên tại Việt Nam
						gia nhập “câu lạc bộ tỷ đô” năm 2021, với lợi nhuận
						trước thuế (LNTT) đạt 23,2 nghìn tỷ đồng, tăng 47,1% so
						với 2020. Đây là năm thứ năm liên tiếp Techcombank ghi
						nhận lợi nhuận tăng trưởng hai chữ số. Ngân hàng cũng
						ghi nhận tốc độ tăng trưởng kép lợi nhuận trong giai
						đoạn 2016-2021 với mức kỷ lục 50%/năm. Bằng cách không
						ngừng truyền cảm hứng cho mỗi tài năng của chúng tôi để
						‘Dare to Be a Greater You’, chúng tôi đặt mục tiêu trở
						thành ngân hàng số 1 Việt Nam với vốn hóa 20 tỷ USD. BỔ
						SUNG: THÔNG ĐIỆP TECHCOMBANK: Đại dịch Covid-19 làm đảo
						lộn nền kinh tế thế giới với những hệ quả cắt giảm ồ ạt
						nhưng không vì thế mà Ngân hàng cắt giảm chi phí đầu tư
						vào việc đào tạo và phát triển Con Người. Với 836.456 số
						giờ đào tạo trực tuyến trong 2021, Techcombank lọt top
						6% công ty có chỉ số cao nhất về Hiệu quả Nhân viên
						trong khu vực Asean. Vừa qua, Chương trình Phát triển
						Năng lực Lãnh đạo được thiết kế thành công dực theo 5
						cấp độ lãnh đạo tại Ngân hàng. Cùng với đó là sự đầu tư
						triển khai rất nhiều khóa đào tạo nghiệp vụ và lãnh đạo
						khác được thiết kế riêng cho từng cấp độ quản lý như:
						TechcomLeader, Future Leaders Program, TechcomHero, vv.
						Bên cạnh Con người, Dữ liệu & Số hóa là những trụ cột
						chiến lược giúp Techcombank có được chỗ đứng trên thị
						trường như ngày hôm nay. Với Ngân hàng, Dữ liệu là kim
						chỉ nam cần thiết giúp khách hàng có những lựa chọn sáng
						suốt và giúp ngân hàng tạo ra các giải pháp phù hợp với
						nhu cầu của từng cá nhân. Ngân hàng tập trung ứng dụng
						công nghệ thông tin trong mọi hoạt động, đưa 90% ứng
						dụng trù định lên đám mây, gia tăng tổng lượng giao dịch
						số lên 70% (đạt 652 triệu), và tăng trưởng 32,3% lượng
						khách hàng số trong 2021. “Văn hóa tổ chức” được xây
						dựng dựa trên 5 Giá trị cốt lõi đã tạo nên sức mạnh của
						Techcombank và là nền tảng cho sự phát triển bền vững
						của tổ chức, mang lại thành công cho khách hàng. Khách
						hàng là trọng tâm: Vì chúng ta chỉ thành công khi khách
						hàng thành công. Đổi mới và sáng tạo: Để luôn dẫn đầu.
						Hợp tác vì mục tiêu chung: Tạo nên sức mạnh tập thể để
						mang lại kết quả vượt trội cho cá nhân và tổ chức. Phát
						triển bản thân: Để có khả năng nắm bắt cơ hội phát triển
						cùng tổ chức. Làm việc hiệu quả: Để mang lại thành công
						lớn hơn với nguồn lực phù hợp.
					</p>

					<textarea
						name="introduce"
						id="introduce"
						rows="5"
						cols="10"
						class="p-2 border border-sky-950 text-xs md:text-sm lg:text-base"
						v-model="introduce"
						v-else
					></textarea>

					<!-- Save   -->
					<div class="flex gap-4">
						<button
							class="px-4 py-2 bg-green-400 rounded-xl text-sky-900 text-xs md:text-sm lg:text-base hover:cursor-pointer hover:opacity-90"
							v-if="isEdittingIntroduce"
							@click="saveIntroduce"
						>
							Lưu
						</button>
					</div>
					<div class="flex gap-4 text-xs md:text-sm lg:text-base">
						<button
							class="bg-green-300 px-4 py-2 rounded-lg font-bold text-sky-900 hover:bg-green-400 hover:cursor-pointer"
						>
							Xem các công việc hiện có
						</button>
						<router-link
							class="border border-green-300 px-4 py-2 rounded-lg text-sky-900 font-semibold hover:cursor-pointer hover:border-green-500"
							to="/companyprofile/recruitmentpost"
						>
							Tạo tin tuyển dụng mới
						</router-link>
					</div>
				</div>
			</div>

			<!-- công việc đang tuyển dụng  -->
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
				<router-link
					to="/companysearch"
					type="button"
					class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800 text-center"
				>
					Xem thêm
				</router-link>
			</div>
		</div>
	</main>
</template>

<script lang="ts">
export default {
	data() {
		return {
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
				{
					id: 3,
					featured: false,
					urgent: false,
					level: "Senior",
					job: "Full Stack Developer",
					desc: "Node.js, Express, MongoDB, React, Vue, Angular",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-3.png",
					salary: "$8K - $12K",
					position: "2",
				},
				{
					id: 4,
					featured: true,
					urgent: false,
					level: "Junior",
					job: "UI/UX Designer",
					desc: "Adobe XD, Sketch, Figma, Photoshop, Illustrator",
					logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-4.png",
					salary: "$4K - $6K",
					position: "4",
				},
			],
			introduce:
				"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
			isEdittingIntroduce: false,
		};
	},
	methods: {
		editIntroduce() {
			this.isEdittingIntroduce = true;
		},
		saveIntroduce() {
			this.isEdittingIntroduce = false;
		},
	},
};
</script>
