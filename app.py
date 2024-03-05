from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Daftar catatan sederhana (digunakan sebagai contoh penyimpanan sederhana)
notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    new_note = request.form.get('note')
    notes.append(new_note)
    return redirect(url_for('index'))

@app.route('/edit_note/<int:index>', methods=['GET', 'POST'])
def edit_note(index):
    if 0 <= index < len(notes):
        if request.method == 'POST':
            edited_note = request.form.get('edited_note')
            notes[index] = edited_note
            return redirect(url_for('index'))
        else:
            return render_template('edit_note.html', index=index, note=notes[index])
    else:
        return redirect(url_for('index'))

@app.route('/delete_note/<int:index>')
def delete_note(index):
    if 0 <= index < len(notes):
        del notes[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
