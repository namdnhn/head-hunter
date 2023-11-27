<template>
	<nav
		class="h-full py-8 px-4 flex flex-col gap-6 items-center bg-white lg:basis-2/5 xl:basis-1/5 w-full overflow-x-scroll min-h-screen max-h-screen overflow-y-auto"
	>
		<div class="flex flex-col justify-center items-center gap-2">
			<img
				src="https://scontent.fhan14-2.fna.fbcdn.net/v/t1.15752-9/380473750_705477890924386_4811766216330519987_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=8cd0a2&_nc_eui2=AeGFmilbrwjAiwoz971chM1LE5bf8IYqo6oTlt_whiqjqh0Iwl9C4uRPI-ZC7gMedieRRXim92lupTLVVeUE-nxV&_nc_ohc=AuDbYUxThqkAX-QdQEU&_nc_ht=scontent.fhan14-2.fna&oh=03_AdSOy_wvf3J7K-ii0QH99UV-lHuv1HBENNtAqOpozA7T7g&oe=6561863A"
				alt="avt"
				class="w-32 h-32 rounded-full"
			/>
			<h2 class="text-sm md:text-base lg:text-lg font-bold text-sky-900">
				Nguyen Duc Thien
			</h2>
			<p class="text-xs md:text-sm lg:text-base text-slate-500">
				Front-end Developer
			</p>
		</div>

		<transition name="detail">
			<div
				class="w-full flex flex-col items-center gap-1"
				v-if="isShowNav"
			>
				<base-list
					title="Thông tin chung"
					icon="fa-solid fa-palette"
					to="/hrdashboard/hrinfo"
				></base-list>
				<base-list
					title="Hồ sơ công ty"
					icon="fa-solid fa-user"
					to="/hrprofile"
				></base-list>
				<base-list
					title="Ứng viên đã lưu"
					icon="fa-solid fa-bookmark"
					to="/hrdashboard/candidatesaved"
				></base-list>
				<base-list
					title="Tin nhắn"
					icon="fa-solid fa-message"
					to="/chat"
				></base-list>
				<base-list
					title="Xóa tài khoản"
					icon="fa-solid fa-trash"
					to="/hrdashboard/deleteaccount"
				></base-list>
				<base-list
					title="Đăng xuất"
					icon="fa-solid fa-right-from-bracket"
					@click="logout"
				></base-list>
			</div>
		</transition>

		<font-awesome-icon
			icon="fa-solid fa-angles-down"
			class="block lg:hidden text-3xl text-green-600 hover:text-green-800 hover:cursor-pointer"
			@click="showNav"
			v-if="!isShowNav"
		/>
		<font-awesome-icon
			icon="fa-solid fa-angles-up"
			class="block lg:hidden text-3xl text-green-600 hover:text-green-800 hover:cursor-pointer"
			@click="showNav"
			v-else
		/>
	</nav>
	<base-spinner v-if="isLoading"></base-spinner>
	<base-dialog :show="!!error" title="Đăng xuất thất bại!" @close="confirmErr"
		><p>
			{{ error }}<br />
			Vui lòng thử lại.
		</p></base-dialog
	>
</template>

<script lang="ts">
export default {
	data() {
		return {
			isLoading: false,
			error: null,
			isShowNav: true,
		};
	},
	methods: {
		logout() {
			try {
				this.$store.dispatch("logout");
				this.isLoading = true;
			} catch (error: any) {
				console.log(error);
				this.error = error.message;
			}
			this.isLoading = false;
			this.$router.push("/loginCandidatePage");
		},
		confirmErr() {
			this.error = null;
		},
		showNav() {
			this.isShowNav = !this.isShowNav;
		},
	},
};
</script>

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
