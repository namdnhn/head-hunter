export default {
	async getCompanies() {
		let apiUrl = "http://localhost:3000/companies";

		const response = await fetch(apiUrl, {
			method: "GET",
			headers: {
				"Content-Type": "application/json",
			},
		});

		const responseData = await response.json();

		if (!response.ok) {
			const error = new Error(
				responseData.message || "Failed to fetch companies."
			);
			throw error;
		}

		return responseData;
	},
	async getCompany(_: any, id: any) {
		let apiUrl = "http://localhost:3000/companies/" + id;

		const response = await fetch(apiUrl, {
			method: "GET",
			headers: {
				"Content-Type": "application/json",
			},
		});

		const responseData = await response.json();

		if (!response.ok) {
			const error = new Error(
				responseData.message || "Failed to fetch company."
			);
			throw error;
		}

		return responseData;
	},
	async createCompany(context: any, payload: any) {
		let apiUrl = await context.rootGetters.getApiUrl;
		apiUrl += "company";

		const response = await fetch(apiUrl, {
			method: "POST",
			body: JSON.stringify({
                user_id: payload.user_id,
				job_quantity: 0,
				name: payload.name,
				address: payload.address,
				founded_year: payload.founded_year ||  0,
				employee_quantity: payload.employee_quantity || 0,
				description: "",
				contact: payload.contact || "",
			}),
			headers: {
				"Content-Type": "application/json",
			},
		});

		const responseData = await response.json();

		if (!response.ok) {
			const error = new Error(
				responseData.message || "Failed to create company."
			);
			throw error;
		}

		context.commit("setCompany", responseData.id);

		return responseData;
	},
};
