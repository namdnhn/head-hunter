<template>
	<nav class="h-full py-8 px-4 flex flex-col gap-6 items-center bg-white lg:basis-2/5 xl:basis-1/5 w-full overflow-x-scroll">
		<div class="flex flex-col justify-center items-center gap-2">
			<img src="https://scontent.fhan14-2.fna.fbcdn.net/v/t1.15752-9/380473750_705477890924386_4811766216330519987_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=8cd0a2&_nc_eui2=AeGFmilbrwjAiwoz971chM1LE5bf8IYqo6oTlt_whiqjqh0Iwl9C4uRPI-ZC7gMedieRRXim92lupTLVVeUE-nxV&_nc_ohc=AuDbYUxThqkAX-QdQEU&_nc_ht=scontent.fhan14-2.fna&oh=03_AdSOy_wvf3J7K-ii0QH99UV-lHuv1HBENNtAqOpozA7T7g&oe=6561863A"
				alt="avt" class="w-32 h-32 rounded-full" />
			<h2 class="text-sm md:text-base lg:text-lg font-bold text-sky-900">
				Nguyen Duc Thien
			</h2>
			<p class="text-xs md:text-sm lg:text-base text-slate-500">Front-end Developer</p>
		</div>

		<ul class="w-full flex flex-col gap-1">
			<base-list title="Thông tin chung" icon="fa-solid fa-palette"></base-list>
			<base-list title="Hồ sơ của tôi" icon="fa-solid fa-user"></base-list>
			<base-list title="CV của tôi" icon="fa-solid fa-file-pdf"></base-list>
			<base-list title="Công việc ứng tuyển" icon="fa-solid fa-paper-plane"></base-list>
			<base-list title="Tin tuyển dụng" icon="fa-solid fa-bell"></base-list>
			<base-list title="Tin tuyển dụng đã lưu" icon="fa-solid fa-bookmark"></base-list>
			<base-list title="Công ty đang theo dõi" icon="fa-solid fa-user-check"></base-list>
			<base-list title="Tin nhắn" icon="fa-solid fa-message"></base-list>
			<base-list title="Đổi mật khẩu" icon="fa-solid fa-key"></base-list>
			<base-list title="Xóa tài khoản" icon="fa-solid fa-trash"></base-list>
			<base-list title="Đăng xuất" icon="fa-solid fa-right-from-bracket"></base-list>
		</ul>
	</nav>
</template>

<style scoped>
::-webkit-scrollbar {
	width: 4px;
	height: 0px;
}

::-webkit-scrollbar-track {
	/* border-radius: 100vh; */
	background: #f7f4ed;
}

::-webkit-scrollbar-thumb {
	background: #94ebbb;
	border-radius: 100vh;
	/* border: 3px solid #f6f7ed; */
}

::-webkit-scrollbar-thumb:hover {
	background: #83d6a8;
}
</style>
