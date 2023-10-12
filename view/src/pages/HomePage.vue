<template>
    <main class="pt-16 lg:pt-20 w-full">
        <div class="w-full bg-yellow-100 px-20 py-10 flex flex-col lg:flex-row gap-6 justify-evenly items-center">
            <section class="text-sky-900">
                <h5 class="text-amber-700 mb-10 font-bold">
                    Khám phá công việc nổi bật và theo xu hướng
                </h5>
                <h1 class="text-3xl md:text-4xl lg:text-5xl mb-10 font-bold">
                    Tìm và tuyển dụng
                    <br />
                    các chuyên gia hàng đầu trên <br />
                    Head Hunter
                </h1>
                <p class="text-sm md:text-base lg:text-lg mb-10">
                    Tìm kiếm công việc không bao giờ là dễ dàng. Hãy kiểm tra những công việc mới chúng tôi
                    <br />
                    sẵn sàng cho bạn trên Head Hunter.
                </p>
                <span>
                    <ul class="flex gap-10 font-bold">
                        <li class="flex flex-col">
                            <h2 class="flex text-3xl md:text-4xl lg:text-5xl gap-2">
                                <span class="text-sky-900">200</span>
                                <span class="text-amber-700">M</span>
                            </h2>
                            <p>Công việc sẵn có</p>
                        </li>
                        <li class="flex flex-col">
                            <h2 class="flex text-3xl md:text-4xl lg:text-5xl gap-2">
                                <span class="text-sky-900">40</span>
                                <span class="text-amber-700">K</span>
                            </h2>
                            <p>Doanh Nghiệp</p>
                        </li>
                        <li class="flex flex-col">
                            <h2 class="flex text-3xl md:text-4xl lg:text-5xl gap-2">
                                <span class="text-sky-900">300</span>
                                <span class="text-amber-700">K</span>
                            </h2>
                            <p>Ứng viên</p>
                        </li>
                    </ul>
                </span>
            </section>

            <!-- Search Jobs -->
            <form action="" class="h-auto p-10 bg-white rounded-lg">
                <h1 class="text-3xl md:text-4xl lg:text-5xl text-sky-900 mb-8 font-bold">
                    Phát triển sự nghiệp của bạn với <br />
                    <span class="text-amber-700">Head Hunter</span>
                </h1>

                <!-- Search jobs keyword  -->
                <div class="relative mb-8">
                    <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                        <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                        </svg>
                    </div>
                    <input type="search"
                        class="block w-full p-4 pl-10 text-xs md:text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder="Tìm kiếm công việc" />
                </div>

                <!-- job level and experience  -->
                <div class="flex gap-12 items-center justify-between mb-8">
                    <span class="flex flex-col w-full">
                        <label for="level" class="text-xs md:text-sm mb-2">Trình độ</label>
                        <select name="level" id="level"
                            class="p-2 border rounded-md min-w-full text-xs md:text-sm lg:text-base">
                            <option value="">Intern</option>
                            <option value="">Fresher</option>
                            <option value="">Junior</option>
                            <option value="">Middle</option>
                            <option value="">Senior</option>
                        </select>
                    </span>

                    <span class="flex flex-col w-full">
                        <label for="experience" class="text-xs md:text-sm mb-2">Kinh nghiệm làm việc</label>
                        <select name="experience" id="experience"
                            class="p-2 border rounded-md min-w-full text-xs md:text-sm lg:text-base">
                            <option value="">Dưới 1 năm</option>
                            <option value="">1 năm</option>
                            <option value="">2 năm</option>
                            <option value="">3 năm</option>
                            <option value="">Trên 4 năm</option>
                        </select>
                    </span>
                </div>

                <!-- expected salary  -->
                <div class="flex gap-12 items-center justify-between mb-8">
                    <span class="flex flex-col w-full">
                        <label for="salary" class="text-xs md:text-sm mb-2">Mức lương</label>
                        <select name="salary" id="salary"
                            class="p-2 border rounded-md min-w-full text-xs md:text-sm lg:text-base">
                            <option value="">Dưới 10 triệu</option>
                            <option value="">10 - 15 triệu</option>
                            <option value="">15 - 20 triệu</option>
                            <option value="">20 - 30 triệu</option>
                            <option value="">30 - 40 triệu</option>
                            <option value="">40 - 50 triệu</option>
                            <option value="">Trên 50 triệu</option>
                            <option value="">Thỏa thuận</option>
                        </select>
                    </span>

                    <span class="flex flex-col w-full">
                        <label for="location" class="text-xs md:text-sm mb-2">Địa điểm làm việc</label>
                        <select name="location" id="location"
                            class="p-2 border rounded-md min-w-full text-xs md:text-sm lg:text-base">
                            <option value="">Tất cả tỉnh/thành phố</option>
                            <option value="">Hà Nội</option>
                            <option value="">TP. Hồ Chí Minh</option>
                            <option value="">Đà Nẵng</option>
                        </select>
                    </span>
                </div>

                <!-- submit button  -->
                <button type="submit"
                    class="bg-sky-900 text-yellow-100 rounded-lg p-4 mt-10 w-full text-xs md:text-sm lg:text-base">
                    Tìm kiếm
                </button>
            </form>
        </div>

        <!-- Featured Jobs -->
        <div class="px-20 py-10 mb-10">
            <span class="text-center">
                <h1 class=" text-xl md:text-2xl lg:text-3xl font-extrabold mb-2 text-sky-900">Công việc nổi bật</h1>
                <!-- <p class="text-xs md:text-sm lg:text-base text-gray-500">
                    Tham gia vào các công việc nổi bật trên Head Hunter
                </p> -->
            </span>

            <!-- Featured Jobs list -->
            <ul class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 mt-10">
                <job-card v-for="job in jobs" :key="job.id" :id="job.id" :featured="job.featured" :urgent="job.urgent" :level="job.level"
                    :job="job.job" :desc="job.desc" :logo="job.logo" :salary="job.salary" :position="job.position">
                </job-card>
            </ul>
        </div>

        <!-- Top job Categories -->
        <div class="px-20 py-10 bg-blue-100">
            <!-- header -->
            <span class="text-center">
                <h1 class="text-xl md:text-2xl lg:text-3xl font-extrabold mb-2 text-sky-900">Khám phá lĩnh vực nổi bật</h1>
                <!-- <p class="text-xs md:text-sm lg:text-base text-gray-500">At vero eos et accusamus et iusto odio dignissimos
                    ducimus qui blanditiis praesentium voluptatum <br>
                    deleniti atque corrupti quos dolores
                </p> -->
            </span>

            <!-- list job category  -->
            <ul class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-10 mb-10">
                <category-card v-for="category in categories" :key="category.id" :icon="category.icon" :job="category.job"
                    :quantity="category.quantity"></category-card>
            </ul>
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
            categories: [
                {
                    id: 1,
                    icon: "fa-solid fa-code",
                    job: "Backend Developer",
                    quantity: 212
                }, {
                    id: 2,
                    icon: "fa-solid fa-computer",
                    job: "Frontend Developer",
                    quantity: 120
                }, {
                    id: 3,
                    icon: "fa-solid fa-robot",
                    job: "AI Engineer",
                    quantity: 76
                },
                {
                    id: 4,
                    icon: "fa-solid fa-database",
                    job: "Data Engineer",
                    quantity: 125
                }
            ]
        }
    }
}

</script>
