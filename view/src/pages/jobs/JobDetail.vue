<template>
    <main class="pt-16 lg:pt-20 w-full h-auto">
        <!-- job header  -->
        <div class="px-10 xl:px-40 pt-20 pb-10 bg-amber-50">
            <div class="flex flex-col md:flex-row gap-6 ">
                <span class="flex flex-col gap-4 items-center">
                    <span class="flex flex-col items-center gap-2">
                        <img src="https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-12.png"
                            alt="company logo" class=" w-28 h-auto">
                        <p class="font-bold text-xs md:text-sm lg:text-base text-sky-900">Công ty ABC</p>
                    </span>
                    <p class="px-3 py-1 bg-orange-400 rounded-lg text-xs lg:text-sm text-white">Đang tuyển 4 vị trí</p>
                </span>

                <div class="flex flex-col gap-8">
                    <div class="flex flex-col gap-2">
                        <span
                            class=" bg-green-200 px-3 py-1 rounded-lg text-green-700 font-semibold text-xs lg:text-sm max-w-max">Senior</span>
                        <h1 class="text-xl md:text-2xl lg:text-3xl font-bold text-sky-900">Front-end Developer</h1>
                        <span class="flex gap-1 text-xs lg:text-sm text-sky-900">
                            <font-awesome-icon icon="fa-solid fa-location-dot" />
                            <address>Cầu Giấy, Hà Nội</address>
                        </span>
                    </div>

                    <div class="flex gap-10">
                        <div>
                            <label class="text-xs md:text-sm lg:text-base font-medium">Vai trò</label>
                            <p class="text-base md:text-lg lg:text-xl font-semibold text-sky-900">Developer</p>
                        </div>
                        <div>
                            <label class="text-xs md:text-sm lg:text-base font-medium">Kinh nghiệm</label>
                            <p class="text-base md:text-lg lg:text-xl font-semibold text-sky-900">7 năm</p>
                        </div>
                    </div>

                    <div class="flex flex-col gap-2">
                        <h2 class="text-xs md:text-sm lg:text-base font-medium">Kỹ năng</h2>
                        <ul
                            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 items-center justify-center">
                            <li class="px-2 py-1 bg-green-200 rounded-lg text-xs text-green-700 flex gap-1 justify-center">
                                <font-awesome-icon icon="fa-regular fa-star" class="text-yellow-500" />
                                <p>HTML5</p>
                            </li>
                            <li class="px-2 py-1 bg-green-200 rounded-lg text-xs text-green-700 flex gap-1 justify-center">
                                <font-awesome-icon icon="fa-regular fa-star" class="text-yellow-500" />
                                <p>CSS3</p>
                            </li>
                            <li class="px-2 py-1 bg-green-200 rounded-lg text-xs text-green-700 flex gap-1 justify-center">
                                <font-awesome-icon icon="fa-regular fa-star" class="text-yellow-500" />
                                <p>Javascript</p>
                            </li>
                            <li class="px-2 py-1 bg-green-200 rounded-lg text-xs text-green-700 flex gap-1 justify-center">
                                <font-awesome-icon icon="fa-regular fa-star" class="text-yellow-500" />
                                <p>NodeJS</p>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- job description and suggest job -->
        <div class="px-10 xl:px-40 pt-4 pb-10 flex flex-col lg:flex-row gap-10">
            <div class="p-4 border border-green-400 rounded-lg flex flex-col justify-between gap-6 lg:basis-3/4">
                <div class="flex flex-col gap-6">
                    <ul class="flex gap-6 text-xs md:text-sm lg:text-base">
                        <li class="px-8 py-1 bg-green-600 text-white rounded-xl hover:cursor-pointer hover:bg-green-700"
                            @click="show('description')">
                            Mô tả
                        </li>
                        <li class="px-8 py-1 bg-green-600 text-white rounded-xl hover:cursor-pointer hover:bg-green-700"
                            @click="show('requirement')">
                            Yêu cầu
                        </li>
                        <li class="px-8 py-1 bg-green-600 text-white rounded-xl hover:cursor-pointer hover:bg-green-700"
                            @click="show('benefit')">
                            Quyền lợi
                        </li>
                    </ul>
    
                    <!-- Job description paragraph  -->
                    <transition name="detail">
                        <div class="flex flex-col gap-4 text-xs md:text-sm lg:text-base text-sky-950" v-if="isShowDescription">
                            <p class=" leading-7">
                                Themezhub Web provides equal employment opportunities to all qualified individuals without
                                regard to
                                race, color, religion, sex, gender identity, sexual orientation, pregnancy, age, national
                                origin,
                                physical or mental disability, military or veteran status, genetic information, or any other
                                protected classification. Equal employment opportunity includes, but is not limited to, hiring,
                                training, promotion, demotion, transfer, leaves of absence, and termination. Thynk Web takes
                                allegations of discrimination, harassment, and retaliation seriously, and will promptly
                                investigate
                                when such behavior is reported.
                            </p>
                            <p class=" leading-7">
                                Our company is seeking to hire a skilled Web Developer to help with the development of our
                                current
                                projects. Your duties will primarily revolve around building software by writing code, as well
                                as
                                modifying software to fix errors, adapt it to new hardware, improve its performance, or upgrade
                                interfaces. You will also be involved in directing system testing and validation procedures, and
                                also working with customers or departments on technical issues including software system design
                                and
                                maintenance.
                            </p>
                            <p class=" leading-7">
                                We are looking for a Senior Web Developer to build and maintain functional web pages and
                                applications. Senior Web Developer will be leading junior developers, refining website
                                specifications, and resolving technical issues. He/She should have extensive experience building
                                web
                                pages from scratch and in-depth knowledge of at least one of the following programming
                                languages:
                                Javascript, Ruby, or PHP. He/She will ensure our web pages are up and running and cover both
                                internal and customer needs.
                            </p>
                        </div>
                    </transition>
    
                    <!-- Yêu cầu  -->
                    <transition name="detail">
                        <div class="flex flex-col gap-4 text-xs md:text-sm lg:text-base" v-if="isShowRequirement">
                            <!-- Yêu cầu công việc  -->
                            <span class="flex flex-col gap-3">
                                <h1 class="text-sm md:text-base lg:text-xl font-bold">Yêu cầu:</h1>
                                <ul class="text-xs md:text-sm lg:text-base flex flex-col gap-2">
                                    <li class="flex items-center gap-2">
                                        <font-awesome-icon icon="fa-regular fa-circle-dot" />
                                        <p>Candidate must have a Bachelors or Masters degree in Computer. (B.tech, Bsc or
                                            BCA/MCA)
                                        </p>
                                    </li>
                                    <li class="flex items-center gap-2">
                                        <font-awesome-icon icon="fa-regular fa-circle-dot" />
                                        <p>Candidate must have a Bachelors or Masters degree in Computer. (B.tech, Bsc or
                                            BCA/MCA)
                                        </p>
                                    </li>
                                    <li class="flex items-center gap-2">
                                        <font-awesome-icon icon="fa-regular fa-circle-dot" />
                                        <p>Candidate must have a Bachelors or Masters degree in Computer. (B.tech, Bsc or
                                            BCA/MCA)
                                        </p>
                                    </li>
                                    <li class="flex items-center gap-2">
                                        <font-awesome-icon icon="fa-regular fa-circle-dot" />
                                        <p>Candidate must have a Bachelors or Masters degree in Computer. (B.tech, Bsc or
                                            BCA/MCA)
                                        </p>
                                    </li>
                                </ul>
                            </span>
    
                            <!-- Công việc cần làm  -->
                            <span class="flex flex-col gap-3">
                                <h1 class="text-sm md:text-base lg:text-xl font-bold">Công việc:</h1>
                                <ul class="text-xs md:text-sm lg:text-base flex flex-col gap-2">
                                    <li class="flex items-center gap-2">
                                        <font-awesome-icon icon="fa-regular fa-circle-dot" />
                                        <p>Write clean, maintainable and efficient code.</p>
                                    </li>
                                    <li class="flex items-center gap-2">
                                        <font-awesome-icon icon="fa-regular fa-circle-dot" />
                                        <p>Candidate must have a Bachelors or Masters degree in Computer. (B.tech, Bsc or
                                            BCA/MCA)
                                        </p>
                                    </li>
                                    <li class="flex items-center gap-2">
                                        <font-awesome-icon icon="fa-regular fa-circle-dot" />
                                        <p>Candidate must have a Bachelors or Masters degree in Computer. (B.tech, Bsc or
                                            BCA/MCA)
                                        </p>
                                    </li>
                                    <li class="flex items-center gap-2">
                                        <font-awesome-icon icon="fa-regular fa-circle-dot" />
                                        <p>Candidate must have a Bachelors or Masters degree in Computer. (B.tech, Bsc or
                                            BCA/MCA)
                                        </p>
                                    </li>
                                </ul>
                            </span>
    
                            <!-- Bằng cấp và kĩ năng  -->
                            <span class="flex flex-col gap-3">
                                <h1 class="text-sm md:text-base lg:text-xl font-bold">Bằng cấp và kĩ năng:</h1>
                                <ul class="text-xs md:text-sm lg:text-base flex flex-col gap-2">
                                    <li class="flex items-center gap-2">
                                        <font-awesome-icon icon="fa-regular fa-circle-dot" />
                                        <p>Write clean, maintainable and efficient code.</p>
                                    </li>
                                    <li class="flex items-center gap-2">
                                        <font-awesome-icon icon="fa-regular fa-circle-dot" />
                                        <p>Candidate must have a Bachelors or Masters degree in Computer. (B.tech, Bsc or
                                            BCA/MCA)
                                        </p>
                                    </li>
                                    <li class="flex items-center gap-2">
                                        <font-awesome-icon icon="fa-regular fa-circle-dot" />
                                        <p>Candidate must have a Bachelors or Masters degree in Computer. (B.tech, Bsc or
                                            BCA/MCA)
                                        </p>
                                    </li>
                                    <li class="flex items-center gap-2">
                                        <font-awesome-icon icon="fa-regular fa-circle-dot" />
                                        <p>Candidate must have a Bachelors or Masters degree in Computer. (B.tech, Bsc or
                                            BCA/MCA)
                                        </p>
                                    </li>
                                </ul>
                            </span>
                        </div>
                    </transition>
    
                    <!-- Quyền lợi  -->
                    <transition name="detail">
                        <div class="flex flex-col gap-4 text-xs md:text-sm lg:text-base" v-if="isShowBenefit">
                            <ul class="text-xs md:text-sm lg:text-base flex flex-col gap-2">
                                <li class="flex items-center gap-2">
                                    <font-awesome-icon icon="fa-regular fa-circle-dot" />
                                    <p>Chính sách phúc lợi đa dạng, hấp dẫn: thưởng nghỉ mát, sinh nhật, thưởng năm học mới,
                                        thưởng
                                        20/11 & thưởng tết nguyên đán; Chế độ khám sức khỏe định kỳ hàng năm.</p>
                                </li>
                            </ul>
                        </div>
                    </transition>
                </div>

                <div class="flex gap-4 text-xs md:text-sm lg:text-base">
                    <button
                        class="bg-green-300 px-4 py-2 rounded-lg font-bold text-sky-900 hover:bg-green-400 hover:cursor-pointer">Ứng
                        tuyển ngay</button>
                    <button
                        class="border border-green-300 px-4 py-2 rounded-lg text-sky-900 font-semibold hover:cursor-pointer hover:border-green-500">Lưu
                        tin</button>
                </div>

            </div>

            <div class="flex flex-col gap-4 lg:basis-1/4">
				<h1 class="text-base md:text-lg lg:text-xl font-bold text-sky-900 mb-4">
					Việc làm tương tự
				</h1>

				<ul class="flex flex-col gap-4">
					<job-card v-for="job in jobs" :key="job.id" :id="job.id" :featured="job.featured" :urgent="job.urgent"
						:level="job.level" :logo="job.logo" :job="job.job" :desc="job.desc" :salary="job.salary"
						:position="job.position"></job-card>
				</ul>

                <button class="text-xs md:text-sm lg:text-base">Xem thêm</button>
			</div>
        </div>
    </main>
</template>

<script lang="ts">
export default {
    // props nhận được khi click từ một job card
    props: ['id', 'featured', 'urgent', 'level', 'logo', 'job', 'desc', 'salary', 'position'],
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
        }
    },
    methods: {
        show(type: String) {
            switch (type) {
                case 'description':
                    this.isShowDescription = true;
                    this.isShowRequirement = false;
                    this.isShowBenefit = false;
                    break;
                case 'requirement':
                    this.isShowDescription = false;
                    this.isShowRequirement = true;
                    this.isShowBenefit = false;
                    break;
                case 'benefit':
                    this.isShowDescription = false;
                    this.isShowRequirement = false;
                    this.isShowBenefit = true;
                    break;
            }
        }
    }
}
</script>

<style scoped>.detail-enter-from {
    opacity: 0;
    transform: translateY(-30px);
}

.detail-enter-to {
    opacity: 1;
    transform: translateY(0);
}

.detail-enter-active {
    transition: all 0.3s ease-out;
}</style>