#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QDir>
#include <QFile>
#include <QMenu>
#include <QProcess>
#include <QSettings>
#include <QThread>

#define SETTINGS_START {
void MainWindow::loadSettings()
{
    QSettings setting("SteamAutoLogin", "settings");
    setting.beginGroup("MainWindow");
    QStringList usernames = setting.value("usernames").value<QStringList>();
    bool hideOnStart = setting.value("hide-on-start", false).toBool();
    setting.endGroup();

    ui->comboBox->addItems(usernames);
    if (hideOnStart) this->hide();
}

void MainWindow::saveSettings()
{
    QStringList usernames;
    for (int i = 0; i < ui->comboBox->count(); i++) {
        QString username = ui->comboBox->itemText(i);
        usernames.append(username);
    }

    QSettings setting("SteamAutoLogin", "settings");
    setting.beginGroup("MainWindow");
    setting.setValue("usernames", usernames);
    setting.endGroup();
}
#define SETTINGS_END }

#define SETUP_START {
MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setupTray();
    loadSettings();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::setupTray()
{
    QAction *showAction = new QAction("Show", this);
    connect(showAction, &QAction::triggered, this, &QWidget::showNormal);

    QAction *quitAction = new QAction("Quit", this);
    connect(quitAction, &QAction::triggered, qApp, &QCoreApplication::quit);

    QMenu *trayIconMenu = new QMenu(this);
    trayIconMenu->addAction(showAction);
    trayIconMenu->addAction(quitAction);

    trayIcon = new QSystemTrayIcon(this);
    trayIcon->setContextMenu(trayIconMenu);

    connect(trayIcon, &QSystemTrayIcon::activated, this, &QWidget::showNormal);
    trayIcon->setIcon(QIcon(":/tray.ico"));
    trayIcon->setToolTip("SteamAutoLogin");
    trayIcon->show();
}
#define SETUP_END }

#define FUNCTIONS_START {
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

    MainWindow::close();
}

void MainWindow::on_removeButton_clicked()
{
    int index = ui->comboBox->currentIndex();
    ui->comboBox->removeItem(index);
    saveSettings();
}

void MainWindow::on_addButton_clicked()
{
    QString username = ui->lineEdit->displayText().toLower();
    ui->comboBox->addItem(username);
    ui->comboBox->setCurrentText(username);
    ui->lineEdit->setText("");
    saveSettings();
}
#define FUNCTIONS_END }
