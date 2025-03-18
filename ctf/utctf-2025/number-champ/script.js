let userUUID = null,
	opponentUUID = null;
var lat = 0,
	lon = 0;
async function findMatch() {
	const e = await fetch(`/match?uuid=${userUUID}&lat=${lat}&lon=${lon}`, {
			method: "POST"
		}),
		t = await e.json();
	t.error ? alert(t.error) : (opponentUUID = t.uuid, document.getElementById("match-info").innerText = `Matched with ${t.user} (Elo: ${t.elo}, Distance: ${Math.round(t.distance)} miles)`, document.getElementById("match-section").style.display = "none", document.getElementById("battle-section").style.display = "block")
}
async function battle() {
	const e = document.getElementById("number-input").value;
	if (!e) return void alert("Please enter a number.");
	const t = await fetch(`/battle?uuid=${userUUID}&opponent=${opponentUUID}&number=${e}`, {
			method: "POST"
		}),
		n = await t.json();
	n.error ? alert(n.error) : (document.getElementById("battle-result").innerText = `Result: ${n.result}. Opponent's number: ${n.opponent_number}. Your new Elo: ${n.elo}`, document.getElementById("user-info").innerText = `Your updated Elo: ${n.elo}`, document.getElementById("battle-section").style.display = "none", document.getElementById("match-section").style.display = "block")
}
window.onload = async () => {
	if (navigator.geolocation) navigator.geolocation.getCurrentPosition((async e => {
		lat = e.coords.latitude, lon = e.coords.longitude;
		const t = await fetch(`/register?lat=${lat}&lon=${lon}`, {
				method: "POST"
			}),
			n = await t.json();
		userUUID = n.uuid, document.getElementById("user-info").innerText = `Welcome, ${n.user}! Elo: ${n.elo}`
	}));
	else {
		alert("Geolocation is not supported by this browser.");
		const e = await fetch(`/register?lat=${lat}&lon=${lon}`, {
				method: "POST"
			}),
			t = await e.json();
		userUUID = t.uuid, document.getElementById("user-info").innerText = `Welcome, ${t.user}! Elo: ${t.elo}`
	}
};
