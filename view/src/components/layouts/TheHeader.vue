<template>
	<header
		class="h-16 lg:h-20 w-full fixed bg-white flex justify-center shadow-md z-50"
	>
		<div class="w-full mx-2 lg:mx-0 lg:w-11/12 flex justify-between">
			<nav class="flex items-center">
				<!-- Menu icon  -->
				<span
					@click="toggleShowMenu"
					class="md:hidden w-6 h-6 mr-4 hover:cursor-pointer hover:text-green-600"
				>
					<font-awesome-icon
						icon="fa-solid fa-bars"
						class="w-6 h-6"
					/>
				</span>

				<!-- Logo -->
				<router-link to="/homepage" class="mr-10 hover:cursor-pointer">
					<img
						src="../../assets/logo.png"
						alt="logo"
						class="w-10 h-10 md:w-12 md:h-12 lg:w-14 lg:h-14 rounded-full"
					/>
				</router-link>

				<!-- Menu bars on small screen -->
				<transition name="menu">
					<ul
						v-show="showMenu"
						class="md:hidden flex flex-col gap-4 absolute top-16 left-0 w-full bg-gray-100"
					>
						<li
							class="mx-2 rounded-md mt-2 p-4 bg-white flex items-center justify-between"
						>
							<router-link
								to="/homepage"
								class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
								>Trang chủ</router-link
							>
						</li>
						<li
							class="mx-2 rounded-md p-4 bg-white flex items-center justify-between"
							@click="toggleMoreInfo('jobs')"
						>
							<a
								class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
								>Việc làm
							</a>
							<font-awesome-icon
								icon="fa-solid fa-chevron-down"
								v-if="!moreInfoJobs"
							/>
							<font-awesome-icon
								icon="fa-solid fa-chevron-up"
								v-else
							/>
						</li>
						<li
							class="mx-2 rounded-md p-4 bg-white flex items-center justify-between"
							@click="toggleMoreInfo('companies')"
							v-if="!isCompany"
						>
							<a
								class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
								>Công ty
							</a>
							<font-awesome-icon
								icon="fa-solid fa-chevron-down"
								v-if="!moreInfoCompanies"
							/>
							<font-awesome-icon
								icon="fa-solid fa-chevron-up"
								v-else
							/>
						</li>
						<li
							class="mx-2 rounded-md mb-2 p-4 bg-white flex items-center justify-between"
							@click="toggleMoreInfo('profiles')"
						>
							<router-link
								to="/profile"
								class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
								>Hồ sơ
							</router-link>
							<font-awesome-icon
								icon="fa-solid fa-chevron-down"
								v-if="!moreInfoProfiles"
							/>
							<font-awesome-icon
								icon="fa-solid fa-chevron-up"
								v-else
							/>
						</li>
					</ul>
				</transition>

				<!-- Menu on large screen -->
				<ul class="hidden md:flex gap-6">
					<li>
						<router-link
							to="/homepage"
							class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
							>Trang chủ</router-link
						>
					</li>
					<li v-if="!isCompany">
						<a
							class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base relative"
							@mouseover="moreInfoJobs = true"
							@mouseleave="moreInfoJobs = false"
							>Việc làm
							<font-awesome-icon
								icon="fa-solid fa-chevron-down"
							/>
							<!-- more info job  -->
							<ul
								class="absolute top-full right-0 w-56 md:w-64 lg:w-80 rounded-lg shadow-md z-10 bg-white flex flex-col items-center justify-center px-4 text-black"
								v-if="moreInfoJobs"
							>
								<base-list
									icon="fa-solid fa-magnifying-glass"
									title="Tìm việc làm"
									@click="moreInfoJobs = false"
									to="/jobsearch"
								/>
								<base-list
									icon="fa-regular fa-heart"
									title="Việc làm đã lưu"
									@click="moreInfoJobs = false"
									to="/userdashboard/jobsaved"
								/>
								<base-list
									icon="fa-solid fa-briefcase"
									title="Việc làm đã ứng tuyển"
									@click="moreInfoJobs = false"
									to="/userdashboard/userinfo"
								/>
							</ul>
						</a>
					</li>
					<li v-if="!isCompany">
						<a
							class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base relative"
							@mouseover="moreInfoCompanies = true"
							@mouseleave="moreInfoCompanies = false"
							>Công ty
							<font-awesome-icon
								icon="fa-solid fa-chevron-down"
							/>
							<!-- more info company -->
							<ul
								class="absolute top-full right-0 w-56 md:w-64 lg:w-80 rounded-lg shadow-md z-10 bg-white flex flex-col items-center justify-center px-4 text-black"
								v-if="moreInfoCompanies"
							>
								<base-list
									icon="fa-solid fa-building"
									title="Tìm kiếm công ty"
									@click="moreInfoCompanies = false"
									to="/companysearch"
								/>
								<base-list
									icon="fa-regular fa-heart"
									title="Công ty đã lưu"
									@click="moreInfoCompanies = false"
									to="/userdashboard/companysaved"
								/>
							</ul>
						</a>
					</li>
					<li>
						<router-link
							:to="candidateProfileLink"
							class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
							v-if="!isCompany"
							>Hồ sơ
						</router-link>
						<router-link
							:to="companyProfileLink"
							class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
							v-if="isCompany"
							>Hồ sơ
						</router-link>
					</li>
					<li>
						<router-link
							to="/chat"
							class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
							>Tin nhắn
						</router-link>
					</li>
                    <li v-if="isCompany">
						<router-link
							:to="companyJobLink"
							class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
							>Công việc đã đăng
						</router-link>
					</li>
                    <li v-if="isCompany">
						<router-link
							to="/candidatesearch"
							class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
							>Ứng viên
						</router-link>
					</li>
				</ul>
			</nav>

			<!-- login, logout  -->
			<span class="flex gap-4 items-center" v-if="!isLoggedIn">
				<router-link
					to="/login"
					class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
					>Đăng nhập</router-link
				>
				<router-link
					to="/register/candidate"
					class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
					>Đăng ký</router-link
				>
			</span>

			<!-- user account info -->
			<span class="flex gap-4 items-center" v-else>
				<span
					class="relative flex items-center gap-2 py-1 px-2 bg-slate-100 rounded-xl hover:cursor-pointer after:content-[''] after:absolute after:w-full after:h-20"
					@mouseover="isShowUserInfo = true"
					@mouseleave="isShowUserInfo = false"
				>
					<img
						:src=" image_path || 'https://www.topcv.vn/images/avatar-default.jpg'"
						alt="default avt"
						class="w-8 h-8 md:w-10 md:h-10 lg:w-12 lg:h-12 object-cover rounded-full"
					/>
					<p class="lg:block text-xs md:text-sm lg:text-base" v-if="!isCompany">
						{{ userInfo.fullname }}
					</p>
                    <p class="lg:block text-xs md:text-sm lg:text-base" v-if="isCompany">
						{{ companyInfo.name }}
					</p>
					<font-awesome-icon icon="fa-solid fa-chevron-down" />
					<!-- more user account info -->
					<ul
						class="absolute top-full right-0 w-56 md:w-64 lg:w-80 rounded-lg shadow-md z-10 bg-white flex flex-col items-center justify-center px-4"
						v-if="isShowUserInfo"
					>
						<base-list
							icon="fa-solid fa-circle-info"
							title="Thông tin tài khoản"
							@click="isShowUserInfo = false"
							to="/userdashboard"
							v-if="!isCompany"
						/>
						<base-list
							icon="fa-solid fa-circle-info"
							title="Thông tin tài khoản"
							@click="isShowUserInfo = false"
							to="/companydashboard"
							v-if="isCompany"
						/>
						<base-list
							icon="fa-solid fa-lock"
							title="Đổi mật khẩu"
							@click="isShowUserInfo = false"
							to="/userdashboard/updateaccount"
							v-if="!isCompany"
						/>
						<base-list
							icon="fa-solid fa-arrow-right-from-bracket"
							title="Đăng xuất"
							@click="logout"
						/>
					</ul>
				</span>
			</span>
		</div>
        <base-dialog :show="!!error" title="Có lỗi xảy ra!">
            <p>Vui lòng thử lại sau.</p>
        </base-dialog>
	</header>
</template>

<script lang="ts">
import BaseList from "../ui/BaseList.vue";
export default {
	components: { BaseList },
	data() {
		return {
			showMenu: false,
			moreInfoJobs: false,
			moreInfoCompanies: false,
			moreInfoProfiles: false,
			loggedIn: false,
			isShowUserInfo: false,
			userId: null,
			userInfo: {
				fullname: "none",
				phone: "",
				date_of_birth: "",
				email: "",
			},
			companyInfo: {
				name: "none",
				email: "",
			},
			companyId: null,
            error: null,
            image_path: "https://www.topcv.vn/images/avatar-default.jpg",
		};
	},
	methods: {
		toggleShowMenu() {
			this.showMenu = !this.showMenu;
		},
		toggleMoreInfo(type: string) {
			switch (type) {
				case "jobs":
					this.moreInfoJobs = !this.moreInfoJobs;
					break;
				case "companies":
					this.moreInfoCompanies = !this.moreInfoCompanies;
					break;
				case "profiles":
					this.moreInfoProfiles = !this.moreInfoProfiles;
					break;
			}
		},
		toggleShowUserInfo() {
			this.isShowUserInfo = !this.isShowUserInfo;
			console.log(this.isShowUserInfo);
		},
		logout() {
			this.$store.dispatch("logout");
			this.$router.push("/homepage");
            window.location.reload();
		},
		async getUserInfo() {
			if (this.isLoggedIn) {
				this.userId = this.$store.getters.userId;
				this.companyId = this.$store.getters.companyId;
                
				try {
					const res = await this.$store.dispatch(
						"fetchUserById",
						this.userId
					);

                    this.image_path = res.image_path;
                    

					//if company
					if (res.role === "candidate") {
						this.userInfo = {
							fullname: res.fullname,
							phone: res.phone,
							date_of_birth: res.date_of_birth,
							email: res.email,
						};
					} else if (res.role === "hr") {
						this.companyInfo = {
							name: res.fullname,
							email: res.email,
						};
                        
					}
				} catch (error: any) {
					//if candidate
					console.log(error);
                    this.error = error;
				}
			} else {
				return;
			}
		},
	},
	computed: {
		isLoggedIn() {
			return this.$store.getters.isAuthenticated;
		},
		candidateProfileLink() {
			return `/candidate/${this.userId}/profile`;
		},
		companyProfileLink() {
			return `/companyprofile/${this.companyId}`;
		},
		isCompany() {
			return this.$store.getters.isCompany;
		},
        companyJobLink() {
            return `/company/${this.companyId}/jobs`
        }
	},
	mounted() {
		this.getUserInfo();
	},
	watch: {
		isLoggedIn() {
			this.getUserInfo();
		},
		isCompany() {
			this.getUserInfo();
		},
	},
};
</script>

<style scoped>
/* user account more info animate  */
.moreInfo-enter-from {
	opacity: 0;
	transform: translateY(-30px);
}

.moreInfo-leave-to {
	opacity: 0;
	transform: translateY(30px);
}

.moreInfo-enter-to,
.moreInfo-leave-from {
	opacity: 1;
	transform: translateY(0);
}

.moreInfo-enter-active {
	transition: all 0.3s ease-out;
}

.moreInfo-leave-active {
	transition: all 0.3s ease-in;
}

/* menu animate  */
.menu-enter-from {
	opacity: 0;
	transform: translateY(-30px);
}

.menu-leave-to {
	opacity: 0;
	transform: translateY(30px);
}

.menu-enter-to,
.menu-leave-from {
	opacity: 1;
	transform: translateY(0);
}

.menu-enter-active {
	transition: all 0.3s ease-out;
}

.menu-leave-active {
	transition: all 0.3s ease-in;
}
</style>
