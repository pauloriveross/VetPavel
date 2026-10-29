import re

path = r"C:\Users\paulo\Downloads\PAGPAVEL\index.html"
with open(path, encoding='utf-8') as f:
    html = f.read()

start = html.index("  var form = document.getElementById('referral');")
end = html.index("})();", start) + len("})();")

lines = [
"  var form = document.getElementById('referral');",
"  if (form) form.addEventListener('submit', function (e) {",
"    e.preventDefault();",
"    if (!form.checkValidity()) { form.reportValidity(); return; }",
"    var clinica = (document.getElementById('clinica')||{}).value || '';",
"    var telefono = (document.getElementById('telefono')||{}).value || '';",
"    var paciente = (document.getElementById('paciente')||{}).value || '';",
"    var motivo = (document.getElementById('motivo')||{}).value || '';",
"    var msg = 'Derivacion: Clinica: ' + clinica + ', Tel: ' + telefono + ', Paciente: ' + paciente + ', Motivo: ' + motivo;",
"    var url = 'https://wa.me/34600123456?text=' + encodeURIComponent(msg);",
"    window.open(url, '_blank');",
"  });",
"})();",
]
new_block = "\n".join(lines)
html = html[:start] + new_block + html[end:]
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print('done')
