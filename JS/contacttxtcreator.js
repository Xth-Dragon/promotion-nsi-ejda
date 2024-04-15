document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = {};

    for (let [key, value] of formData.entries()) {
        data[key] = value;
    }

    const txtData = [
        'Nom: ' + data.nom,
        'Prénom: ' + data.prenom,
        'Adresse Email: ' + data.email,
        'Numéro de téléphone: ' + data.tel,
        'Date de naissance: ' + data.dateNaissance,
        // 'Genre: ' + gender, ne fonctionne pas
        'Adresse: ' + data.adresse + ', ' + data.ville + ', ' + data.region + ', ' + data.codePostal + ', ' + data.pays,
        'Commentaire: ' + data.commentaire
    ].join('\n');

    const blob = new Blob([txtData], {type: 'text/plain'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'contactinfos.txt';
    a.click();
});
