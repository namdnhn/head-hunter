<template>
	<main class="pt-16 lg:pt-20 h-auto">
		<!-- Introduce  -->
		<div
			class="bg-gray-100 px-10 md:px-24 lg:px-40 xl:px-60 py-10 flex flex-col lg:flex-row gap-6 justify-between items-center"
		>
			<div class="flex flex-col md:flex-row items-center gap-6">
				<img
					src="https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/team-1.jpg"
					alt="candidate avt"
					class="w-32 md:w-40 lg:w-48 h-auto rounded-full"
				/>
				<div
					class="flex flex-col justify-between items-center md:items-start gap-2 text-center md:text-start"
				>
					<h4
						class="text-base md:text-lg lg:text-xl font-semibold text-sky-950"
					>
						Nguyễn Đức Thiện
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
								class="mr-1"
							/>
							Software Developer
						</li>
						<li
							class="text-gray-700 text-xs md:text-sm lg:text-base"
						>
							<font-awesome-icon
								icon="fa-solid fa-location-dot"
								class="mr-1"
							/>
							Hà Nội
						</li>
						<li
							class="text-gray-700 text-xs md:text-sm lg:text-base"
						>
							<font-awesome-icon
								icon="fa-solid fa-cake-candles"
								class="mr-1"
							/>11-01-2003
						</li>
					</ul>

					<!-- skills  -->
					<ul class="grid grid-cols-3 gap-4 mt-4 text-center">
						<li
							class="text-gray-500 bg-gray-200 text-xs md:text-sm lg:text-base py-1 px-4  rounded-lg"
						>
							Design
						</li>
						<li
							class="text-gray-500 text-xs md:text-sm lg:text-base py-1 px-4 bg-gray-200 rounded-lg"
						>
							PHP
						</li>
						<li
							class="text-gray-500 text-xs md:text-sm lg:text-base py-1 px-4 bg-gray-200 rounded-lg"
						>
							NodeJS
						</li>
						<li
							class="text-gray-500 text-xs md:text-sm lg:text-base py-1 px-4 bg-gray-200 rounded-lg"
						>
							WordPress
						</li>
						<li
							class="text-gray-500 text-xs md:text-sm lg:text-base py-1 px-4 bg-gray-200 rounded-lg"
						>
							VueJS
						</li>
						<li
							class="text-gray-500 text-xs md:text-sm lg:text-base py-1 px-4 bg-gray-200 rounded-lg"
						>
							Python
						</li>
					</ul>
				</div>
			</div>

			<div class="flex flex-col h-full justify-between">
				<!-- <font-awesome-icon icon="fa-solid fa-pen-to-square" class="text-3xl"/> -->
				<span
					class="p-4 bg-sky-900 rounded-lg text-yellow-100 hover:cursor-pointer hover:opacity-95 text-xs md:text-sm lg:text-base"
					>Đăng CV
					<font-awesome-icon icon="fa-solid fa-upload" class="ml-2" />
				</span>
			</div>
		</div>

		<!-- Detail info and suggest jobs  -->
		<div
			class="px-10 md:px-24 lg:px-40 py-10 flex flex-col lg:flex-row lg:gap-10"
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
						{{ introduce }}
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
							Save
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
						/>
					</span>
					<ul class="grid grid-cols-1 gap-6 md:grid-cols-2">
						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-envelope"
								class="bg-slate-200 text-xl text-green-600 p-4 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ personalInfo.email }}
								</h5>
								<input
									type="text"
									class="px-2 py-1 border border-sky-950"
									v-else
									v-model="personalInfo.email"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Email
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-phone"
								class="bg-slate-200 text-xl text-green-600 p-4 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ personalInfo.phoneNumber }}
								</h5>
								<input
									type="text"
									class="px-2 py-1 border border-sky-950"
									v-else
									v-model="personalInfo.phoneNumber"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Số điện thoại
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-user"
								class="bg-slate-200 text-xl text-green-600 p-4 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ personalInfo.gender }}
								</h5>
								<input
									type="text"
									class="px-2 py-1 border border-sky-950"
									v-else
									v-model="personalInfo.gender"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Giới tính
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-cake-candles"
								class="bg-slate-200 text-xl text-green-600 p-4 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ personalInfo.dob }}
								</h5>
								<input
									type="text"
									class="px-2 py-1 border border-sky-950"
									v-else
									v-model="personalInfo.dob"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Ngày sinh
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-wallet"
								class="bg-slate-200 text-xl text-green-600 p-4 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ personalInfo.expectedSalary }}
								</h5>
								<input
									type="text"
									class="px-2 py-1 border border-sky-950"
									v-else
									v-model="personalInfo.expectedSalary"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Mức lương mong muốn
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-briefcase"
								class="bg-slate-200 text-xl text-green-600 p-4 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ personalInfo.experience }}
								</h5>
								<input
									type="text"
									class="px-2 py-1 border border-sky-950"
									v-else
									v-model="personalInfo.experience"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Kinh nghiệm
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-graduation-cap"
								class="bg-slate-200 text-xl text-green-600 p-4 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ personalInfo.degree }}
								</h5>
								<input
									type="text"
									class="px-2 py-1 border border-sky-950"
									v-else
									v-model="personalInfo.degree"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Bằng cấp
								</p>
							</span>
						</li>

						<li class="flex gap-4 items-center">
							<font-awesome-icon
								icon="fa-solid fa-layer-group"
								class="bg-slate-200 text-xl text-green-600 p-4 rounded-lg"
							/>
							<span>
								<h5
									class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
									v-if="!isEdittingPersonalInfo"
								>
									{{ personalInfo.level }}
								</h5>
								<input
									type="text"
									class="px-2 py-1 border border-sky-950"
									v-else
									v-model="personalInfo.level"
								/>

								<p class="text-xs lg:text-sm text-gray-500">
									Trình độ
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
							Save
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
						/>
					</span>

					<ul class="flex flex-col gap-4">
						<experience-card
							v-for="company in companies"
							:key="company.id"
							:id="company.id"
							:isEditting="isEdittingJobs"
							v-model:name="company.name"
							v-model:duration="company.duration"
							v-model:role="company.role"
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
							Save
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
						/>
					</span>

					<ul class="flex flex-col gap-4">
						<experience-card
							v-for="education in educations"
							:key="education.id"
							:id="education.id"
							:isEditting="isEdittingEducation"
							v-model:name="education.name"
							v-model:duration="education.duration"
							v-model:role="education.role"
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
							Save
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
						/>
					</span>

					<ul class="flex gap-4">
						<li
							class="py-2 px-4 text-center text-gray-500 bg-gray-200 rounded-xl text-xs md:text-sm lg:text-base"
                            v-for="skill in skills" :key="skill.id"
						>
							{{ skill.name }}
                            <font-awesome-icon icon="fa-solid fa-xmark" class="text-green-700 text-xs md:text-sm lg:text-base hover:cursor-pointer" @click="deleteSkills(skill.id)" v-if="isEdittingSkills"/>
						</li>
						
					</ul>

                    <!-- Save   -->
					<div class="flex gap-4">
						<button
							class="px-4 py-2 bg-green-400 rounded-xl text-sky-900 text-xs md:text-sm lg:text-base hover:cursor-pointer hover:opacity-90"
							v-if="isEdittingSkills"
							@click="saveSkills"
						>
							Lưu
						</button>

                        <button
							class="px-4 py-2 bg-green-400 rounded-xl text-sky-900 text-xs md:text-sm lg:text-base hover:cursor-pointer hover:opacity-90"
							v-if="isEdittingSkills"
							@click="addSkills"
						>
							Thêm
						</button>
					</div>
				</div>

				<!-- Language  -->
				<div
					class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10"
				>
					<span class="flex justify-between">
					    <h1
    						class="text-base md:text-lg lg:text-xl font-bold text-sky-900"
    					>
    						Ngôn ngữ
    					</h1>
                        <font-awesome-icon
							icon="fa-solid fa-pen-to-square"
							class="text-xs md:text-sm lg:text-base text-green-700 hover:cursor-pointer"
							@click="editLanguage"
						/>
					</span>

					<ul
						class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-10 lg:gap-20"
					>
						<li class="flex gap-2 items-center">
							<h1
								class="py-1 md:py-2 lg:py-3 px-2 md:px-3 lg:px-4 rounded-full bg-green-300 font-bold text-center text-sm md:text-base lg:text-lg"
							>
								JP
							</h1>
							<span>
								<h2
									class="text-xs md:text-sm lg:text-base font-semibold text-sky-900"
								>
									Japanese
								</h2>
								<p class="text-gray-500 text-xs lg:text-sm">
									Basic
								</p>
							</span>
						</li>

						<li class="flex gap-2 items-center">
							<h1
								class="py-1 md:py-2 lg:py-3 px-2 md:px-3 lg:px-4 rounded-full bg-green-300 font-bold text-center text-sm md:text-base lg:text-lg"
							>
								EN
							</h1>
							<span>
								<h2
									class="text-xs md:text-sm lg:text-base font-semibold text-sky-900"
								>
									English
								</h2>
								<p class="text-gray-500 text-xs lg:text-sm">
									Advance
								</p>
							</span>
						</li>

						<li class="flex gap-2 items-center">
							<h1
								class="py-1 md:py-2 lg:py-3 px-2 md:px-3 lg:px-4 rounded-full bg-green-300 font-bold text-center text-sm md:text-base lg:text-lg"
							>
								CN
							</h1>
							<span>
								<h2
									class="text-xs md:text-sm lg:text-base font-semibold text-sky-900"
								>
									Chinese
								</h2>
								<p class="text-gray-500 text-xs lg:text-sm">
									Medium
								</p>
							</span>
						</li>
					</ul>
				</div>

				<!-- CV  -->
				<div
					class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10"
				>
					<h1
						class="text-base md:text-lg lg:text-xl font-bold text-sky-900"
					>
						CV
					</h1>

					<ul class="flex flex-col gap-4">
						<cv-card
							v-for="card in cv"
							:key="card.id"
							:fileName="card.fileName"
							:time="card.time"
						></cv-card>
					</ul>
				</div>
			</div>

			<!-- suggest jobs  -->
			<div class="lg:basis-1/3">
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
			</div>
		</div>
	</main>
</template>

<script lang="ts">
export default {
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
            skills: [
                { id: 1, name: "Java" },
                { id: 2, name: "Python" },
                { id: 3, name: "VueJS" },
                { id: 4, name: "NodeJS" },
            ],
			introduce:
				"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
			isEdittingIntroduce: false,
			personalInfo: {
				email: "abcd@gmail.com",
				phoneNumber: "123456789",
				gender: "Male",
				dob: "01-01-2023",
				expectedSalary: "None",
				experience: "None",
				degree: "None",
				level: "None",
			},
			isEdittingPersonalInfo: false,
			isEdittingJobs: false,
			isEdittingEducation: false,
            isEdittingSkills: false,
            isEdittingLanguage: false
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
		},
		addCompany() {
			const newCompany = {
				id: this.companies.length + 1,
				name: "Tên công ty",
				role: "Vai trò",
				duration: "Thời gian làm việc",
			};
			this.companies.push(newCompany);
		},
		deleteCompany(id: Number) {
			this.companies = this.companies.filter(
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
                id: this.educations.length + 1,
                name: "Tên trường",
                role: "Ngành",
                duration: "Thời gian học"
            }
            this.educations.push(newEducation)
        },
		deleteEducation(id: Number) {
			this.educations = this.educations.filter(
				(education) => education.id !== id
			);
		},
        editSkills() {
            this.isEdittingSkills = true
        },
        deleteSkills(id: Number) {
            this.skills = this.skills.filter(
                (skill) => skill.id !== id
            )
        },
        addSkills() {
            const newSkill = {
                id: this.skills.length + 1,
                name: "Kỹ năng"
            }
            this.skills.push(newSkill)
        },
        saveSkills() {
            this.isEdittingSkills = false
        },
        editLanguage() {
            this.isEdittingLanguage = true
        },
	},
};
</script>
