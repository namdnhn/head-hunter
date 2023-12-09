<template>
	<main class="pt-16 lg:pt-20 h-auto w-full">
		<!-- Introduce  -->

		<div
			class="bg-gray-100 px-10 lg:px-20 xl:px-40 py-10 flex flex-col lg:flex-row gap-6 justify-between items-center"
		>
			<div class="flex flex-col md:flex-row items-center gap-6">
				<div class="flex flex-col gap-2 items-center">
					<label for="uploadAvt" class="hover:cursor-pointer">
						<img
							:src="uploadedImage || imagePreview || image_path"
							alt="candidate avt"
							class="w-32 h-32 md:w-40 md:h-40 lg:w-56 lg:h-56 rounded-full"
						/>
					</label>
					<button
						class="bg-green-400 px-2 py-1 rounded text-sky-900 max-w-fit"
						v-if="imagePreview"
						@click="uploadImage"
					>
						Lưu
					</button>
					<input
						type="file"
						@change="previewImage"
						accept="image/*"
						id="uploadAvt"
						class="hidden"
						ref="fileInput"
					/>
				</div>
				<div
					class="flex flex-col justify-between items-center md:items-start gap-2 text-center md:text-start"
				>
					<h4
						class="text-base md:text-lg lg:text-xl font-semibold text-sky-950"
					>
						{{ accountInfo.fullname }}
					</h4>
					<!-- info  -->
					<ul
						class="flex gap-4 items-center text-center md:text-start"
					>
						<li
							class="text-gray-700 text-xs md:text-sm lg:text-base"
						>
							<font-awesome-icon
								icon="fa-solid fa-user-tie"
								class="mr-1 text-green-600"
							/>
							{{ personalInfo.insight }}
						</li>
						<li
							class="text-gray-700 text-xs md:text-sm lg:text-base"
						>
							<font-awesome-icon
								icon="fa-solid fa-location-dot"
								class="mr-1 text-green-600"
							/>
							{{ personalInfo.location }}
						</li>
						<li
							class="text-gray-700 text-xs md:text-sm lg:text-base"
						>
							<font-awesome-icon
								icon="fa-solid fa-cake-candles"
								class="mr-1 text-green-600"
							/>{{ accountInfo.date_of_birth }}
						</li>
					</ul>
				</div>
			</div>
		</div>

		<!-- Detail info and suggest jobs  -->
		<div
			class="px-10 lg:px-20 xl:px-40 py-10 flex flex-col lg:flex-row lg:gap-10 w-full"
		>
			<!-- User info  -->
			<div class="w-full">
				<!-- introduce  -->
				<div
					class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10 w-full"
				>
					<span class="flex justify-between w-full">
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
							v-if="!isCompany"
						/>
					</span>

					<!-- Paragraph  -->
					<p
						class="text-xs md:text-sm lg:text-base text-gray-600"
						v-if="!isEdittingIntroduce"
					>
						{{ cvProfile.introduce }}
					</p>

					<textarea
						name="introduce"
						id="introduce"
						rows="5"
						cols="10"
						class="p-2 border border-sky-950 text-xs md:text-sm lg:text-base"
						v-model="cvProfile.introduce"
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
				</div>

				<!-- all info  -->
				<div
					class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10"
				>
					<span class="flex justify-between">
						<h1
							class="text-base md:text-lg lg:text-xl font-bold text-sky-900"
						>
							Thông tin cá nhân
						</h1>
						<font-awesome-icon
							icon="fa-solid fa-pen-to-square"
							class="text-xs md:text-sm lg:text-base text-green-700 hover:cursor-pointer"
							@click="editPersonalInfo"
							v-if="!isCompany"
						/>
					</span>
					<ul class="grid grid-cols-1 gap-6 md:grid-cols-2">
						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-envelope"
								class="bg-slate-200 text-xl text-green-600 p-4 w-6 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ cvProfile.email }}
								</h5>
								<input
									type="text"
									class="text-xs md:text-sm lg:text-base px-2 py-1 w-full border border-sky-950"
									v-else
									v-model="cvProfile.email"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Email
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-phone"
								class="bg-slate-200 text-xl text-green-600 p-4 w-6 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ cvProfile.phone }}
								</h5>
								<input
									type="text"
									class="text-xs md:text-sm lg:text-base px-2 py-1 w-full border border-sky-950"
									v-else
									v-model="cvProfile.phone"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Số điện thoại
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-user"
								class="bg-slate-200 text-xl text-green-600 p-4 w-6 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ cvProfile.gender }}
								</h5>
								<input
									type="text"
									class="text-xs md:text-sm lg:text-base px-2 py-1 w-full border border-sky-950"
									v-else
									v-model="cvProfile.gender"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Giới tính
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-cake-candles"
								class="bg-slate-200 text-xl text-green-600 p-4 w-6 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ cvProfile.date_of_birth }}
								</h5>
								<input
									type="text"
									class="text-xs md:text-sm lg:text-base px-2 py-1 w-full border border-sky-950"
									v-else
									v-model="cvProfile.date_of_birth"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Ngày sinh
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-user-tie"
								class="bg-slate-200 text-xl text-green-600 p-4 w-6 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ cvProfile.role }}
								</h5>
								<input
									type="text"
									class="text-xs md:text-sm lg:text-base px-2 py-1 w-full border border-sky-950"
									v-else
									v-model="cvProfile.role"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Lĩnh vực
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-briefcase"
								class="bg-slate-200 text-xl text-green-600 p-4 w-6 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ cvProfile.year_experience }}
								</h5>
								<input
									type="text"
									class="text-xs md:text-sm lg:text-base px-2 py-1 w-full border border-sky-950"
									v-else
									v-model="cvProfile.year_experience"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Kinh nghiệm
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-graduation-cap"
								class="bg-slate-200 text-xl text-green-600 p-4 w-6 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ cvProfile.degree }}
								</h5>
								<input
									type="text"
									class="text-xs md:text-sm lg:text-base px-2 py-1 w-full border border-sky-950"
									v-else
									v-model="cvProfile.degree"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Bằng cấp
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-location-dot"
								class="bg-slate-200 text-xl text-green-600 p-4 w-6 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ cvProfile.current_address }}
								</h5>
								<input
									type="text"
									class="text-xs md:text-sm lg:text-base px-2 py-1 w-full border border-sky-950"
									v-else
									v-model="cvProfile.current_address"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Nơi ở hiện tại
								</p>
							</span>
						</li>
					</ul>
					<!-- Save   -->
					<div class="flex gap-4">
						<button
							class="px-4 py-2 bg-green-400 rounded-xl text-sky-900 text-xs md:text-sm lg:text-base hover:cursor-pointer hover:opacity-90"
							v-if="isEdittingPersonalInfo"
							@click="savePersonalInfo"
						>
							Lưu
						</button>
					</div>
				</div>

				<!-- Experience  -->
				<div
					class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10"
				>
					<span class="flex justify-between">
						<h1
							class="text-base md:text-lg lg:text-xl font-bold text-sky-900"
						>
							Kinh nghiệm làm việc
						</h1>

						<font-awesome-icon
							icon="fa-solid fa-pen-to-square"
							class="text-xs md:text-sm lg:text-base text-green-700 hover:cursor-pointer"
							@click="editJobs"
							v-if="!isCompany"
						/>
					</span>

					<ul class="flex flex-col gap-4">
						<experience-card
							v-for="company in cvProfile.experiences"
							:key="company.id"
							:id="company.id"
							:isEditting="isEdittingJobs"
							v-model:name="company.company"
							v-model:duration="company.time"
							@delete-experience="deleteCompany"
						></experience-card>
					</ul>

					<!-- Add / Save   -->
					<div class="flex gap-4">
						<button
							class="px-4 py-2 bg-green-400 rounded-xl text-sky-900 text-xs md:text-sm lg:text-base hover:cursor-pointer hover:opacity-90"
							v-if="isEdittingJobs"
							@click="saveJobs"
						>
							Lưu
						</button>

						<button
							class="px-4 py-2 bg-green-400 rounded-xl text-sky-900 text-xs md:text-sm lg:text-base hover:cursor-pointer hover:opacity-90"
							v-if="isEdittingJobs"
							@click="addCompany"
						>
							Thêm
						</button>
					</div>
				</div>

				<!-- Education  -->
				<div
					class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10"
				>
					<span class="flex justify-between">
						<h1
							class="text-base md:text-lg lg:text-xl font-bold text-sky-900"
						>
							Học vấn
						</h1>

						<font-awesome-icon
							icon="fa-solid fa-pen-to-square"
							class="text-xs md:text-sm lg:text-base text-green-700 hover:cursor-pointer"
							@click="editEducation"
							v-if="!isCompany"
						/>
					</span>

					<ul class="flex flex-col gap-4">
						<experience-card
							v-for="education in cvProfile.educations"
							:key="education.id"
							:id="education.id"
							:isEditting="isEdittingEducation"
							v-model:name="education.school"
							v-model:duration="education.time"
							@delete-experience="deleteEducation"
						></experience-card>
					</ul>

					<!-- Save   -->
					<div class="flex gap-4">
						<button
							class="px-4 py-2 bg-green-400 rounded-xl text-sky-900 text-xs md:text-sm lg:text-base hover:cursor-pointer hover:opacity-90"
							v-if="isEdittingEducation"
							@click="saveEducation"
						>
							Lưu
						</button>

						<button
							class="px-4 py-2 bg-green-400 rounded-xl text-sky-900 text-xs md:text-sm lg:text-base hover:cursor-pointer hover:opacity-90"
							v-if="isEdittingEducation"
							@click="addEducation"
						>
							Thêm
						</button>
					</div>
				</div>

				<!-- Candidate skill  -->
				<div
					class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10"
				>
					<span class="flex justify-between">
						<h1
							class="text-base md:text-lg lg:text-xl font-bold text-sky-900"
						>
							Kỹ năng
						</h1>

						<font-awesome-icon
							icon="fa-solid fa-pen-to-square"
							class="text-xs md:text-sm lg:text-base text-green-700 hover:cursor-pointer"
							@click="editSkills"
							v-if="!isCompany"
						/>
					</span>

					<div class="flex flex-col gap-4">
						<div class="grid grid-cols-2">
							<label for="skill">Ngôn ngữ lập trình: </label>
							<input
								type="text"
								id="skill"
								class="border px-2 py-1 rounded border-black"
								v-if="isEdittingSkills"
								v-model="cvProfile.skill"
							/>
							<p v-else>{{ cvProfile.skill }}</p>
						</div>
						<div class="grid grid-cols-2">
							<label for="language">Ngoại ngữ: </label>
							<input
								type="text"
								id="language"
								class="border px-2 py-1 rounded border-black"
								v-if="isEdittingSkills"
								v-model="cvProfile.language"
							/>
							<p v-else>{{ cvProfile.language }}</p>
						</div>
					</div>

					<!-- Save   -->
					<div class="flex gap-4">
						<button
							class="px-4 py-2 bg-green-400 rounded-xl text-sky-900 text-xs md:text-sm lg:text-base hover:cursor-pointer hover:opacity-90"
							v-if="isEdittingSkills"
							@click="saveSkills"
						>
							Lưu
						</button>
					</div>
				</div>

				<!-- CV  -->
				<div
					class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10"
				>
					<span class="flex justify-between">
						<h1
							class="text-base md:text-lg lg:text-xl font-bold text-sky-900"
						>
							CV
						</h1>
						<font-awesome-icon
							icon="fa-solid fa-pen-to-square"
							class="text-xs md:text-sm lg:text-base text-green-700 hover:cursor-pointer"
							@click="editCV"
							v-if="!isCompany"
						/>
					</span>

					<div class="flex justify-between items-center">
						<a
							v-if="cvProfile.cv"
							:href="cvProfile.cv"
							target="_blank"
							class="flex gap-2 items-center text-xs md:text-sm lg:text-base text-sky-900 font-semibold hover:cursor-pointer"
						>
							<font-awesome-icon
								icon="fa-solid fa-file-lines"
								class="bg-slate-200 text-xl text-green-600 p-4 w-6 rounded-lg"
							/>
							My CV
						</a>

						<font-awesome-icon
							icon="fa-solid fa-xmark"
							class="text-green-700 hover:cursor-pointer"
							v-if="isEdittingCV && cvProfile.cv"
							@click="deleteCv"
						/>
					</div>

					<div
						class="flex flex-col items-start gap-2"
						v-if="isEdittingCV"
					>
						<input
							type="file"
							@change="handleFileUpload"
							accept=".pdf"
							ref="pdfInput"
						/>
						<button
							@click="uploadFile"
							v-if="selectedFile"
							class="bg-green-400 px-2 py-1 rounded-lg text-sky-900"
						>
							Tải lên
						</button>
					</div>
				</div>
			</div>

			<!-- <div
				class="h-96 w-full flex justify-center items-center"
				v-if="!hasCvProfile"
			>
				<h1
					class="text-base md:text-lg lg:text-xl xl:text-2xl flex gap-1 text-sky-900 font-bold"
				>
					Bạn chưa có CV nào,
					<p
						class="text-red-500 hover:cursor-pointer hover:text-red-600"
						@click="addCvProfile"
					>
						hãy tạo CV ngay bây giờ!
					</p>
				</h1>
			</div> -->

			<!-- suggest jobs  -->
			<!-- <div class="lg:basis-1/3 hidden">
				<h1
					class="text-base md:text-lg lg:text-xl font-bold text-sky-900 mb-4"
				>
					Việc làm phù hợp với bạn
				</h1>

				<ul class="flex flex-col gap-4">
					<job-card
						v-for="job in jobs"
						:key="job.id"
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
			</div> -->
		</div>
		<base-spinner v-if="isLoading"></base-spinner>
	</main>
</template>

<script lang="ts">
import LanguageCard from "../../components/profile/LanguageCard.vue";
import {
	getStorage,
	ref,
	uploadBytesResumable,
	getDownloadURL,
} from "firebase/storage";
import {app} from "../../../services/app";
export default {
	components: {
		LanguageCard,
	},
	props: ["id"],
	data() {
		return {
			companies: [
				{
					id: 1,
					name: "Google Inc.",
					role: "Sr. Team Leader",
					duration: "Feb 2017 - Present",
				},
				{
					id: 2,
					name: "Linked In",
					role: "Sr. Product Designer",
					duration: "Aug 2015 - Jan 2017",
				},
			],
			educations: [
				{
					id: 1,
					name: "Vietnam National University, Hanoi",
					role: "Bachelor of Computer Science",
					duration: "Sep 2021 - Sep 2025",
				},
			],
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
			cv: [
				{ id: 1, fileName: "CV1.pdf", time: "12-12-2021" },
				{ id: 2, fileName: "CV2.pdf", time: "12-12-2021" },
			],
			languages: [
				{ id: 1, name: "English", level: "Advance" },
				{ id: 2, name: "Japanese", level: "Basic" },
				{ id: 3, name: "Chinese", level: "Medium" },
			],
			introduce:
				"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
			isEdittingIntroduce: false,
			personalInfo: {
				email: "abcd@gmail.com",
				phoneNumber: "123456789",
				gender: "Male",
				dob: "01-01-2023",
				insight: "Software Developer",
				experience: "1 năm",
				degree: "Cử nhân CNTT",
				location: "Hà Nội",
				avatarUrl: "https://www.topcv.vn/images/avatar-default.jpg", // set a default image URL here
			},
			accountInfo: {
				fullname: "undefined",
				email: "undefined",
				phone: "undefined",
				date_of_birth: "undefined",
			},
			isEdittingPersonalInfo: false,
			isEdittingJobs: false,
			isEdittingEducation: false,
			isEdittingSkills: false,
			isEdittingLanguage: false,
			isEdittingCV: false,
			imagePreview: null as string | null,
			imageFile: null as File | null,
			uploadedImage: null as string | null,
			selectedFile: null as File | null,
			cvProfile: {
				introduce: "",
				email: "",
				phone: "",
				gender: "",
				date_of_birth: "",
				role: "",
				year_experience: "",
				degree: "",
				current_address: "",
				experiences: [{ time: "", company: "", role: "" }],
				educations: [{ school: "", time: "", department: "" }],
				skill: "",
				language: "",
				cv: "",
				avatar: "",
			},
			hasCvProfile: false,
			isLoading: false,
			image_path: "https://www.topcv.vn/images/avatar-default.jpg",
		};
	},
	methods: {
		editIntroduce() {
			this.isEdittingIntroduce = true;
		},
		saveIntroduce() {
			this.isEdittingIntroduce = false;
		},
		editPersonalInfo() {
			this.isEdittingPersonalInfo = true;
		},
		savePersonalInfo() {
			this.isEdittingPersonalInfo = false;
		},
		editJobs() {
			this.isEdittingJobs = true;
		},
		saveJobs() {
			this.isEdittingJobs = false;
			console.log(this.cvProfile);
		},
		addCompany() {
			const newCompany = {
				id: this.cvProfile.experiences.length + 1,
				company: "Tên công ty",
				time: "Thời gian làm việc",
			};
			this.cvProfile.experiences.push(newCompany);
		},
		deleteCompany(id: Number) {
			this.cvProfile.experiences = this.cvProfile.experiences.filter(
				(company) => company.id !== id
			);
		},
		editEducation() {
			this.isEdittingEducation = true;
		},
		saveEducation() {
			this.isEdittingEducation = false;
		},
		addEducation() {
			const newEducation = {
				id: this.cvProfile.educations.length + 1,
				school: "Tên trường",
				department: "Ngành học",
				time: "Thời gian học",
			};
			this.cvProfile.educations.push(newEducation);
		},
		deleteEducation(id: Number) {
			this.cvProfile.educations = this.cvProfile.educations.filter(
				(education) => education.id !== id
			);
		},
		editSkills() {
			this.isEdittingSkills = true;
		},
		deleteSkills(id: Number) {
			this.skills = this.skills.filter((skill) => skill.id !== id);
		},
		saveSkills() {
			this.isEdittingSkills = false;
		},
		addLanguage() {
			const newLanguage = {
				id: this.languages.length + 1,
				name: "Ngôn ngữ",
				level: "Trình độ",
			};
			this.languages.push(newLanguage);
		},
		deleteLanguage(id: Number) {
			this.languages = this.languages.filter(
				(language) => language.id !== id
			);
		},
		editCV() {
			this.isEdittingCV = true;
		},
		saveCV() {
			this.isEdittingCV = false;
		},
		deleteCv() {
			this.cvProfile.cv = "";
		},
		previewImage(event: Event) {
			const file = (event.target as HTMLInputElement).files?.[0];
			if (file) {
				this.imageFile = file;
				const reader = new FileReader();
				reader.onload = (e) => {
					this.imagePreview = e.target?.result as string | null;
				};
				reader.readAsDataURL(file);
			}
		},
		deleteImage() {
			this.imagePreview = null;
			this.imageFile = null;
			(this.$refs.fileInput as HTMLInputElement).value = "";
		},
		async uploadImage() {
			if (this.imageFile) {
                this.isLoading = true
				const storage = getStorage(app);
				const storageRef = ref(
					storage,
					"images/" + this.imageFile.name
				);

				const uploadTask = uploadBytesResumable(
					storageRef,
					this.imageFile
				);

				try {
					await new Promise((resolve, reject) => {
						uploadTask.on(
							"state_changed",
							(snapshot) => {
								const progress =
									(snapshot.bytesTransferred /
										snapshot.totalBytes) *
									100;
								console.log("Upload is " + progress + "% done");
							},
							(error) => {
								console.error("Upload failed:", error);
								reject(error);
							},
							() => {
								resolve(uploadTask.snapshot);
							}
						);
					});

					const downloadURL = await getDownloadURL(
						uploadTask.snapshot.ref
					);
					console.log("File available at", downloadURL);
					this.uploadedImage = downloadURL;
					this.image_path = downloadURL;
					await this.updateImagePath();
					this.deleteImage();
				} catch (error) {
					console.error("Upload failed:", error);
				}
			}
            this.isLoading = false
		},
		handleFileUpload(event: any) {
			this.selectedFile = event.target.files[0];
		},
		async uploadFile() {
			if (this.selectedFile) {
				await this.uploadPDF(this.selectedFile);
				this.isEdittingCV = false;
				this.cvFileName = this.selectedFile.name;
			} else {
				console.error("No file selected for upload");
			}
		},
		async uploadPDF(file: any) {
			this.isLoading = true;
			const storage = getStorage();
			const storageRef = ref(storage, "pdfs/" + file.name);

			const uploadTask = uploadBytesResumable(storageRef, file);

			const uploadPromise = new Promise((resolve, reject) => {
				uploadTask.on(
					"state_changed",
					(snapshot) => {
						const progress =
							(snapshot.bytesTransferred / snapshot.totalBytes) *
							100;
						console.log("Upload is " + progress + "% done");
					},
					(error) => {
						console.error("Upload failed:", error);
						reject(error);
					},
					() => {
						getDownloadURL(uploadTask.snapshot.ref).then(
							(downloadURL) => {
								console.log("File available at", downloadURL);
								this.cvProfile.cv = downloadURL;
								this.selectedFile = null;
								(
									this.$refs.pdfInput as HTMLInputElement
								).value = "";
								resolve(downloadURL);
							}
						);
					}
				);
			});

			try {
				await uploadPromise;
			} catch (error) {
				console.error("Upload failed:", error);
			} finally {
				this.isLoading = false;
			}
		},
		async getAccountInfo() {
			try {
				await this.$store.dispatch("fetchUserById", this.id);
				this.accountInfo = this.$store.getters.getUserInfo;
				console.log(this.accountInfo);

				//convert date_of_birth to display
				const date = new Date(this.accountInfo.date_of_birth);
				const year = date.getFullYear();
				const month = date.getMonth() + 1;
				const dt = date.getDate();
				const displayDate = dt + "-" + month + "-" + year;
				this.accountInfo.date_of_birth = displayDate;
			} catch (error) {
				console.log(error);
			}
		},
		async getProfile() {
			const userId = this.$store.getters.userId;
			console.log(this.id);
			try {
				const result = await this.$store.dispatch(
					"cv/getCvByUserId",
					this.id
				);

				if (result) {
					this.cvProfile = result;
					this.cvProfile.date_of_birth =
						this.accountInfo.date_of_birth;
				} else {
					const formData = {
						experiences: [{ time: "", company: "", role: "" }],
						educations: [{ school: "", time: "", department: "" }],
						cv: {
							user_id: this.id,
							introduce: "",
							email: this.accountInfo.email,
							phone: this.accountInfo.phone,
							gender: "",
							date_of_birth: this.accountInfo.date_of_birth,
							role: "",
							year_experience: "",
							degree: "",
							current_address: "",
							skill: "",
							language: "",
							cv: "",
							avatar: "",
						},
					};
					const resCreateCv = await fetch(
						"http://localhost:8000/api/cv/create",
						{
							method: "POST",
							headers: {
								"Content-Type": "application/json",
							},
							body: JSON.stringify(formData),
						}
					);
					const responseData = await resCreateCv.json();
					console.log(responseData);
					this.cvProfile = responseData;
				}

				//convert date_of_birth to display
				if (this.cvProfile) {
					this.hasCvProfile = true;
				}
				console.log(this.cvProfile);
			} catch (error) {
				console.log(error);
			}
		},
		async addCvProfile() {
			this.hasCvProfile = true;
		},
		async getImagePath() {
			const res = await fetch(
				`http://localhost:8000/api/user/${this.id}`
			);

			const responseData = await res.json();

			this.image_path = responseData.image_path;
		},
		async updateImagePath() {
			const formData = {
				image_path: this.image_path,
			};

			const res = await fetch(
				`http://localhost:8000/api/user/update/profile/${this.id}`,
				{
					method: "PUT",
					headers: {
						"Content-Type": "application/json",
					},
					body: JSON.stringify(formData),
				}
			);

			const responseData = await res.json();

			console.log(responseData);
		},
	},
	computed: {
		isLoggedIn() {
			return this.$store.getters.isAuthenticated;
		},
		isCompany() {
			return this.$store.getters.isCompany;
		},
	},
	mounted() {
		this.getAccountInfo();
		this.getProfile();
		this.getImagePath();
	},
	watch: {
		isLoggedIn() {
			this.getAccountInfo();
		},
		isCompany() {
			this.getAccountInfo();
		},
	},
};
</script>
