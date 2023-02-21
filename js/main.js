
const viewQRcode = (payment_id) => {
    const qrcodeElem = document.getElementById("qrcode")

    new QRCode(qrcodeElem, {
        text: payment_id,
        width: 350,
        height: 350,
        colorDark: "#000000",
        colorLight: "#ffffff",
    })
}
