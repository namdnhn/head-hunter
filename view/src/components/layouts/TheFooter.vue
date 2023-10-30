<template>
    <footer class="px-20 pt-20 pb-10 bg-sky-950 flex flex-col gap-20 static z-10">
        <div class="grid gap-10 grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
            <div class="flex flex-col gap-4 items-center">
                <h1 class="flex items-center gap-2 text-xl md:text-2xl lg:text-3xl font-bold text-amber-100">
                    <img src="../../assets/logo.png"
                        alt="logo head hunter"
                        class=" w-12 md:w-14 lg:w-16 rounded-full">
                    Head Hunter
                </h1>
                <address class="text-xs md:text-sm lg:text-base text-stone-400">144 Xuân Thủy, Cầu Giấy, Hà Nội</address>
                <span class="flex gap-4 text-lg md:text-xl lg:text-2xl text-stone-400">
                    <font-awesome-icon icon="fa-brands fa-facebook" class="hover:cursor-pointer hover:opacity-90"/>
                    <font-awesome-icon icon="fa-brands fa-linkedin" class="hover:cursor-pointer hover:opacity-90"/>
                    <font-awesome-icon icon="fa-brands fa-google" class="hover:cursor-pointer hover:opacity-90"/>
                </span>
            </div>

            <div class="flex flex-col gap-3 items-center text-stone-400">
                <h1 class="text-sm md:text-base lg:text-lg text-amber-100">Dành cho ứng viên</h1>
                <ul class="text-xs md:text-sm lg:text-base flex flex-col gap-2 items-center">
                    <li class="hover:cursor-pointer hover:text-stone-500">
                        Tìm việc
                    </li>
                    <li class="hover:cursor-pointer hover:text-stone-500">
                        Khám phá doanh nghiệp
                    </li>
                    <li class="hover:cursor-pointer hover:text-stone-500">
                        Hồ sơ cá nhân
                    </li>
                </ul>
            </div>

            <div class="flex flex-col gap-3 items-center text-stone-400">
                <h1 class="text-sm md:text-base lg:text-lg text-amber-100">Dành cho doanh nghiệp</h1>
                <ul class="text-xs md:text-sm lg:text-base flex flex-col gap-2 items-center">
                    <li class="hover:cursor-pointer hover:text-stone-500">
                        Tìm ứng viên
                    </li>
                    <li class="hover:cursor-pointer hover:text-stone-500">
                        Khám phá ứng viên
                    </li>
                    <li class="hover:cursor-pointer hover:text-stone-500">
                        Đăng tin tuyển dụng
                    </li>
                </ul>
            </div>

            <div class="flex flex-col gap-3 text-stone-400 items-center ">
                <h1 class="text-sm md:text-base lg:text-lg text-amber-100">Về Head Hunter</h1>
                <ul class="text-xs md:text-sm lg:text-base flex flex-col gap-2 items-center">
                    <li class="hover:cursor-pointer hover:text-stone-500">
                        Giới thiệu
                    </li>
                    <li class="hover:cursor-pointer hover:text-stone-500">
                        Liên lạc
                    </li>
                    <li class="hover:cursor-pointer hover:text-stone-500">
                        Hỗ trợ
                    </li>
                </ul>
            </div>

        </div>
    </footer>
</template>