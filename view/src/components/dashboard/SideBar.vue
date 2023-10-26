<template>
	<nav
		class="h-full py-8 px-4 flex flex-col gap-6 items-center bg-white basis-1/4 w-full overflow-x-scroll"
	>
		<div class="flex flex-col justify-center items-center gap-2">
			<img
				src="../../assets/headHunterLogo.png"
				alt="avt"
				class="w-24 h-auto rounded-full"
			/>
			<h2 class="text-xs md:text-sm lg:text-base font-bold text-sky-900">
				Nguyen Duc Thien
			</h2>
			<p class="text-xs lg:text-sm text-slate-500">Front-end Developer</p>
		</div>

		<ul class="w-full">
			<base-list
				title="Thông tin chung"
				icon="fa-solid fa-palette"
			></base-list>
			<base-list
				title="Hồ sơ của tôi"
				icon="fa-solid fa-user"
			></base-list>
			<base-list
				title="CV của tôi"
				icon="fa-solid fa-file-pdf"
			></base-list>
			<base-list
				title="Công việc ứng tuyển"
				icon="fa-solid fa-paper-plane"
			></base-list>
			<base-list
				title="Tin tuyển dụng"
				icon="fa-solid fa-bell"
			></base-list>
			<base-list
				title="Tin tuyển dụng đã lưu"
				icon="fa-solid fa-bookmark"
			></base-list>
			<base-list
				title="Công ty đang theo dõi"
				icon="fa-solid fa-user-check"
			></base-list>
			<base-list title="Tin nhắn" icon="fa-solid fa-message"></base-list>
			<base-list title="Đổi mật khẩu" icon="fa-solid fa-key"></base-list>
			<base-list
				title="Xóa tài khoản"
				icon="fa-solid fa-trash"
			></base-list>
			<base-list
				title="Đăng xuất"
				icon="fa-solid fa-right-from-bracket"
			></base-list>
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
