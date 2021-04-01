#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QDir>
#include <QFile>
#include <QProcess>
#include <QSettings>
#include <QThread>
#include <QDebug>

QStringList LoadSettings()
{
    QSettings setting("SteamAutoLogin", "settings");
    setting.beginGroup("MainWindow");
    QStringList usernames = setting.value("usernames").value<QStringList>();
    setting.endGroup();

    return usernames;
}

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QStringList usernames = LoadSettings();
    ui->comboBox->addItems(usernames);
}

void SaveSettings(QComboBox* comboBox)
{
    QStringList usernames;
    for (int i = 0; i < comboBox->count(); i++) {
        QString username = comboBox->itemText(i);
        usernames.append(username);
    }

    QSettings setting("SteamAutoLogin", "settings");
    setting.beginGroup("MainWindow");
    setting.setValue("usernames", usernames);
    setting.endGroup();
}

MainWindow::~MainWindow()
{
    SaveSettings(ui->comboBox);

    delete ui;
}

void MainWindow::on_loginButton_clicked()
{
    system("killall --quiet --wait steam");

    QString username = ui->comboBox->currentText().toLower();
    QFile file(QDir::homePath() + "/.steam/registry.vdf");
    file.open(QIODevice::ReadWrite);
    QByteArray fileData = file.readAll();
    QString text(fileData);
    QRegularExpression re = QRegularExpression("\"AutoLoginUser\".+");
    text.replace(re, "\"AutoLoginUser\"         \"" + username + "\"");
    file.seek(0);
    file.write(text.toUtf8());
    file.close();

    QProcess process;
    process.setProgram("steam");
    process.setStandardOutputFile(QProcess::nullDevice());
    process.setStandardErrorFile(QProcess::nullDevice());
    process.startDetached();

    exit(0);
}

void MainWindow::on_removeButton_clicked()
{
    int index = ui->comboBox->currentIndex();
    ui->comboBox->removeItem(index);
}

void MainWindow::on_addButton_clicked()
{
    QString username = ui->lineEdit->displayText().toLower();
    ui->lineEdit->setText("");
    ui->comboBox->addItem(username);
    ui->comboBox->setCurrentText(username);
}
