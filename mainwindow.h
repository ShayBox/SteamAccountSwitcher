#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QSystemTrayIcon>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void createTrayIcon();
    void on_loginButton_clicked();
    void on_removeButton_clicked();
    void on_addButton_clicked();

private:
    Ui::MainWindow *ui;
    QSystemTrayIcon *trayIcon;
};
#endif // MAINWINDOW_H
